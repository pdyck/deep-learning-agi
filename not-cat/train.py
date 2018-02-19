from lenet import LeNet
from data import get_data

epochs = 25
lr = 1e-3
batch_size = 32

model = LeNet()
(x_train, y_train), (x_test, y_test) = get_data()
print(x_test[0])
print(y_test[0])
