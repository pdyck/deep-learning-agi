from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD

def XOR():
    model = Sequential()
    model.add(Dense(8, input_dim=2))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    return model
