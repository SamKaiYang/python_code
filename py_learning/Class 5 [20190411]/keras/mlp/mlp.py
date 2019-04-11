from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
import keras.utils as np_utils
import numpy as np
import matplotlib.pyplot as plt
import time as t
import pandas as pd
import pickle

EPOCHS = 10
BATCH_SIZe = 200
SHOW_PANDAS_INFO = True
SHOW_TRAIN_IMAGE = False
SHOW_TEST_IMAG = False
SHOW_TRAIN_HISTORY = True
np.random.seed(10)

weights_name = "mlp_weights_" + "epochs_" + str(EPOCHS)

def show_train_history(train_history, train, validation):
    plt.plot(train_history[train])
    plt.plot(train_history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap='binary')
    plt.show()

def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    '''show image and its label'''
    fig = plt.gcf()
    fig.set_size_inches(12, 10)
    if num > 25 : num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1+i)
        ax.imshow(images[idx], cmap='binary')
        title = 'label=' + str(labels[idx])
        if len(prediction) > 0:
            title += ", prediction=" + str(prediction[idx])
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_Train = x_train.reshape(60000, 784).astype('float32')
x_Test = x_test.reshape(10000, 784).astype('float32')
x_Train_Norm = x_Train/255
x_Test_Norm = x_Test/255
y_Train = np_utils.to_categorical(y_train)
y_Test = np_utils.to_categorical(y_test)

#show data info
print('Type of x_Train_Norm: ', type(x_Train_Norm))
print('Lens of x_Train_Norm: ', len(x_Train_Norm))
print('Shape of x_Train_Norm: ', x_Train_Norm.shape)

model = Sequential()
model.add(Dense(units=256, input_shape=(784,), activation='relu'))
model.add(Dense(units=256, activation='relu'))
model.add(Dense(units=10,  activation='softmax'))

#show network info
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

try :
    model.load_weights("mpl_weights/" + weights_name + ".h5")
    print("Loading weights.")
except:
    print("Train new weights.")
    train_history = model.fit(x=x_Train_Norm, y=y_Train, validation_split=0.2, epochs=EPOCHS, batch_size=BATCH_SIZe, verbose=1)
    with open("mlp_train_history/train_history_" + weights_name, "wb") as fout:
            pickle.dump(train_history.history, fout)

model.save_weights("mpl_weights/" + weights_name + ".h5")

scores = model.evaluate(x_Test_Norm, y_Test)

if SHOW_TRAIN_HISTORY:
    with open("mlp_train_history/train_history_" + weights_name, "rb") as fin:
        train_history = pickle.load(fin)
    show_train_history(train_history, 'acc', 'val_acc')

time = t.time()
prediction = model.predict_classes(x_Test_Norm)
time = t.time()- time

print('accuracy: ', scores[1])
print('prediction time: ', time)

if SHOW_TRAIN_IMAGE:
    plot_images_labels_prediction(x_train, y_train, [], 0, 25)

if SHOW_PANDAS_INFO:
    df = pd.DataFrame({'label': y_test, 'predict': prediction})
    print(pd.crosstab(y_test, prediction, rownames=['label'], colnames=['predict']))
    print(df[(df.label==5)&(df.predict==6)])

if SHOW_TEST_IMAG:
    plot_images_labels_prediction(x_test, y_test, prediction, idx=9982, num=1)