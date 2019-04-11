from keras.datasets import cifar10
from keras.utils import np_utils
from keras import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
import matplotlib.pyplot as plt
import numpy as np
np.random.seed(10)

label_dict = {0:"airplane", 1:"automobile", 2:"bird", 3:"cat", 4:"deer", \
    5:"dog", 6:"frog", 7:"horse", 8:"ship", 9:"truck"}

def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    '''show image and its label'''
    fig = plt.gcf()
    fig.set_size_inches(12, 10)
    if num > 25 : num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1+i)
        ax.imshow(images[idx], cmap='binary')

        title = str(i) + ',' + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()

(X_Train, Y_Train), (X_Test, Y_Test) = cifar10.load_data()

X_Train4D_normalize = X_Train.astype('float32')/255.0
X_Test4D_normalize = X_Test.astype('float32')/255.0
Y_trainOneHot = np_utils.to_categorical(Y_Train)
Y_TestOneHot = np_utils.to_categorical(Y_Test)

model = Sequential()

model.add(Conv2D(filters=16, kernel_size=(3, 3), padding='same', input_shape=(32, 32, 3), activation='relu'))

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


train_histroy = model.fit(x=X_Train4D_normalize, y=Y_trainOneHot, verbose=1, \
    epochs=10, validation_split=0.2, batch_size=128)
