from model import XOR
from data import load_data
from keras.optimizers import SGD

X, Y = load_data()
model = XOR()

model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.1))
model.fit(X, Y, batch_size=1, epochs=1000)

print(model.predict_proba(X))
