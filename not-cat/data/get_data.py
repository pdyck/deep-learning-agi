import glob
import random
import os
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical

def split_data(data, ratio=0.8):
    split_index = int(len(data) * ratio)
    return data[:split_index], data[split_index:]

def get_data():
    data = []
    labels = []

    image_paths = glob.glob('data/images/*/*.jpg')
    random.shuffle(image_paths)

    for image_path in image_paths:
        image = cv2.imread(image_path)
        image = cv2.resize(image, (28, 28))
        image = img_to_array(image)
        data.append(image)

        label = image_path.split(os.path.sep)[-2]
        label = 1 if label == 'cat' else 0
        labels.append(label)

    data = np.array(data, dtype='float') / 255.0
    labels = np.array(labels)

    x_train, x_test = split_data(data)
    y_train, y_test = split_data(labels)

    y_train = to_categorical(y_train, num_classes=2)
    y_test = to_categorical(y_test, num_classes=2)

    return (x_train, y_train), (x_test, y_test)
