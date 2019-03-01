import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
	return 1/(1 + np.exe(-x))
	
x = np.array([-1.0,1.0,2.0])
	
print(sigmoid(x))
	
