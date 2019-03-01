import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0,50,100]


print(iris.feature_names)
print(iris.target_names)
print(iris.data_names)
print(iris.target[0])

