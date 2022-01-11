import sys
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import os
import numpy as np
from skimage.transform import rescale
# from skimage.color import rgb2gray
from skimage.measure import LineModelND, ransac
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential



# https://azure.microsoft.com/en-us/try/cognitive-services/my-apis/
API_KEY = os.getenv('AZURE_CV_KEY')
if not API_KEY:
    print('You need to get an azure CV api key and assign it to the environmental variable AZURE_CV_KEY')


def azure_ocr(im_data, key=API_KEY):
    """
    Send image data to azure computer vision api for OCR.
    """


    endpoint = "https://5914reconcile.cognitiveservices.azure.com"
    credential = AzureKeyCredential(key)

    form_recognizer_client = FormRecognizerClient(endpoint, credential)

    receipt = im_data

    poller = form_recognizer_client.begin_recognize_receipts(receipt)
    result = poller.result()

    retRept = []
    for receipt in result:
        for name, field in receipt.fields.items():
            if name == "Items":
                print("Receipt Items:")
                for idx, items in enumerate(field.value):
                    print("...Item #{}".format(idx+1))
                    s = []
                    for item_name, item in items.value.items():
                        print("......{}: {} has confidence {}".format(item_name, item.value, item.confidence))
                        s.append([item_name, item.value, item.confidence])
                    retRept.append(s)
            else:
                print("{}: {} has confidence {}".format(name, field.value, field.confidence))
                retRept.append([name, field.value, field.confidence])
    return retRept
    
    


def read_receipt(im_data):
    
    # Hit the Azure API
    response_dict = azure_ocr(im_data)
    if not response_dict:
        raise ValueError('There was a problem reading your photo')

    return response_dict



if __name__=='__main__':


    import io
    fn = '../data/receipt_preprocessed.jpg'
    # buf = io.BytesIO()
    # plt.imsave(buf, im)
    # im_data = buf.getvalue()
    with open(fn, 'rb') as f:
        im_data = f.read()

    receipt_dict = read_receipt(im_data)
    for key, val in receipt_dict.items():
        print(key, val)
        print()

    
