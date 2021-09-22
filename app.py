from flask import (
    Flask , Blueprint, flash, g, redirect, render_template, request, jsonify, session, url_for
)
from preprocess import preprocess_image
from read_receipt_image import read_receipt
import io
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def im_to_json(im):
    """Here's where the magic happens"""

    preprocessed_im = preprocess_image(im)


    buf = io.BytesIO()
    plt.imsave(buf, preprocessed_im)
    im_data = buf.getvalue()

    bill_dict = read_receipt(im_data)

    return jsonify(bill_dict)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/api/v1/read", methods=["POST", "GET"])
def home():
    print(request.files)
    if 'file' in request.files:
        im = plt.imread(request.files['file'])
        return im_to_json(im)
    else:
        # return im_to_json(None)
        print('Received request with no image attached')
        return 'Request should have an image file attached'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')