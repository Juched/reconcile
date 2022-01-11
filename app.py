from flask import (
    Flask , Blueprint, flash, g, redirect, render_template, request, jsonify, session, url_for
)
import os

from read_receipt_image import read_receipt
import io
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pickle
import uuid
import json
import datetime

class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime) or isinstance(z, datetime.date) or isinstance(z, datetime.time):
            return (str(z))
        else:
            return super().default(z)




UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def im_to_json(im):
    """Here's where the magic happens"""


    buf = io.BytesIO()
    plt.imsave(buf, im)
    im_data = buf.getvalue()

    bill_dict = read_receipt(im_data)

    return bill_dict

@app.route("/api/v1/receipts", methods=["GET"])
def receipts():
    receipts = []
    for filename in os.listdir('receipts/'):
        with open(os.path.join(os.getcwd(),'receipts',  filename), 'rb') as f: 
            receipts.append(pickle.load(f))

    return json.dumps(receipts,cls=DateTimeEncoder)

@app.route('/receipt/<r>')
def receipt(r):
    return

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/v1/read", methods=["POST", "GET"])
def home():
    print(request.files)
    if 'file' in request.files:
        im = plt.imread(request.files['file'])
        bill = im_to_json(im)
        print(type(bill))
        print(bill)
        unique_filename = uuid.uuid4()
        file_pi = open(f'receipts/{unique_filename.hex}.receipt', 'wb') 
        pickle.dump(bill, file_pi)
        file_pi.close()
        return "Completed"
    else:
        # return im_to_json(None)
        print('Received request with no image attached')
        return 'Request should have an image file attached'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')