from keras.datasets import mnist
from keras.utils import np_utils
from keras import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
import numpy as np
np.random.seed(10)

(X_Train, Y_Train), (X_Test, Y_Test) = mnist.load_data()
X_Train4D = X_Train.reshape(X_Train.shape[0], 28, 28, 1).astype('float32')
X_Test4D = X_Test.reshape(X_Test.shape[0], 28, 28, 1).astype('float32')
X_Train4D_normalize = X_Train4D/255
X_Test4D_normalize = X_Test4D/255
Y_trainOneHot = np_utils.to_categorical(Y_Train)
Y_TestOneHot = np_utils.to_categorical(Y_Test)

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=(5, 5), padding='same', input_shape=(28, 28, 1), activation='relu'))

model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(5, 5), padding='same', activation='relu'))

model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(units=128, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(units=10,activation='softmax'))

print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


train_histroy = model.fit(x=X_Train4D_normalize, y=Y_trainOneHot, verbose=1, epochs=10, validation_split=0.2, batch_size=300)

score = model.evaluate(X_Test4D_normalize, Y_TestOneHot)

print('accuracy: ', score[1])
