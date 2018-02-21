from lenet import LeNet
from data.get_data import get_data
import cv2
import numpy as np
from keras.preprocessing.image import img_to_array

(x_train, y_train), (x_test, y_test) = get_data()

model = LeNet()
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=32,
          epochs=14,
          verbose=1,
          validation_data=(x_test, y_test))

model.save('cat_not_cat.h5')

# image = cv2.imread('tiger.jpg')
# image = cv2.resize(image, (28, 28))
# image = img_to_array(image)
# image = np.array([image], dtype='float') / 255.0

# print(model.predict_proba(image))
