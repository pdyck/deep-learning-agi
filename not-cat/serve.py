from flask import Flask, request
from keras.models import load_model
from urllib.request import urlopen
import numpy as np
import cv2
from keras.preprocessing.image import img_to_array

app = Flask(__name__)
model = load_model('cat_not_cat.h5')

@app.route('/predict', methods=['GET'])
def predict():
    url = request.args.get('url')
    req = urlopen(url)
    arr = np.array(bytearray(req.read()), dtype='uint8')
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    image = np.array([image], dtype='float') / 255.0

    prediction = model.predict(image)
    not_cat = prediction[0][0]
    cat = prediction[0][1]

    img_tag = '<img width="500" src="' + url + '">'

    if cat > not_cat:
        percentage = str(round(cat * 100, 2)) + '% Katze'
    else:
        percentage = str(round(not_cat * 100, 2)) + '% keine Katze'

    percentage = '<h1>' + percentage + '</h1>'

    return img_tag + percentage

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
