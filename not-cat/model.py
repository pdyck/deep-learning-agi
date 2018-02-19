from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import SeperableConv2D, Conv2D
from keras.layers import BatchNormalization, GlobalAveragePooling2D

def ConvolutionLayer(filters, kernel, strides):
    x = SeperableConv2D(filters, kernel, strides=strides, padding='same')
    x = BatchNormalization()(x)
    return Activation('elu')(x)

def DeepDog(input_shape):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), strides=(2, 2), padding='same'))

    model.add(ConvolutionLayer(32, (3, 3), (1, 1)))
    model.add(ConvolutionLayer(64, (3, 3), (2, 2)))
    model.add(ConvolutionLayer(128, (3, 3), (1, 1)))
    model.add(ConvolutionLayer(128, (3, 3), (2, 2)))
    model.add(ConvolutionLayer(256, (3, 3), (1, 1)))
    model.add(ConvolutionLayer(256, (3, 3), (2, 2)))

    for _ in range(5):
        model.add(ConvolutionLayer(512, (3, 3), (1, 1)))

    model.add(ConvolutionLayer(512, (3, 3), (2, 2)))
    model.add(ConvolutionLayer(1024, (3, 3), (1, 1)))

    model.add(GlobalAveragePooling2D())

    model.add(Dense(1, activation='sigmoid'))

    return model
