import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

SHOW_PREDICTION = True
SHOW_DATA = False

def plot_data(X, Y):
    # plot data
    plt.scatter(X, Y)
    plt.show()

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))

if SHOW_DATA:
    plot_data(X, Y)

X_train, Y_train = X[:160], Y[:160]     # train 前 160 data points
X_test, Y_test = X[160:], Y[160:]       # test 后 40 data points
print("Type of X_train:", type(X_train))
print("Shape of X_train:", X_train.shape)

model = Sequential()
model.add(Dense(units = 1, input_dim=1))

# choose loss function and optimizing method
model.compile(loss='mse', optimizer='sgd')
model.summary()
'''
# training
print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print('train cost: ', cost)
'''

train_history = model.fit(x=X_train, y=Y_train, validation_split=0.2, epochs=100, batch_size=20, verbose=1)

# test
print('\nTesting ------------')
cost = model.evaluate(X_test, Y_test, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

if SHOW_PREDICTION:
    # plotting the prediction
    Y_pred = model.predict(X_test)
    plt.scatter(X_test, Y_test)
    plt.scatter(X_test, Y_pred)
    plt.show()
