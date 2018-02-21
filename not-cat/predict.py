import flask
import cv2
import glob
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model

images = glob.glob('*.jpg')
for image_path in images:
    print(image_path)
    image = cv2.imread(image_path)
    image = cv2.resize(image, (28, 28))
    image = img_to_array(image)
    image = np.array([image], dtype='float') / 255.0

    model = load_model('cat_not_cat.h5')
    prediction = model.predict(image)

    print(prediction)
