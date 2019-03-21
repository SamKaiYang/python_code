from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
import keras.utils as np_utils
import matplotlib.pyplot as plt

EPOCHS = 10
BATCH_SIZe = 200

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

model = Sequential()
model.add(Dense(units=256, input_shape=(784,), activation='relu'))
model.add(Dense(units=10,  activation='softmax'))

#show network info
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
train_history = model.fit(x=x_Train_Norm, y=y_Train, validation_split=0.2, epochs=EPOCHS, batch_size=BATCH_SIZe, verbose=1)
print("model.evaluate: ")
scores = model.evaluate(x_Test_Norm, y_Test)
prediction = model.predict_classes(x_Test_Norm)
print('accuracy: ', scores[1])
plot_images_labels_prediction(x_test, y_test, prediction, 500, 25)