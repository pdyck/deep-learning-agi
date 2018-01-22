from model import LeNet
from data import load_data

(x_train, y_train), (x_test, y_test) = load_data()
model = LeNet()

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=128,
          epochs=12,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)

print('Loss', score[0])
print('Accuracy', score[1])
