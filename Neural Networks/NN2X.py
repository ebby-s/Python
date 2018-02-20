import numpy as np
np.random.seed(1)

def sigmoid (X,deriv = False):
    if deriv == True:
        return X*(1-X)
    return 1/(1+np.exp(-X))

def train(number):
    global weighting
    global y
    global l0
    global l1
    global l1_error
    global l1_delta
    weighting = 2*np.random.random((4,1))-1
    for iter in range(100000):
        l0 = number
        l1 = sigmoid(np.dot(l0,weighting))
        l1_error = y - l1
        l1_delta = l1_error*sigmoid(l1,True)
        weighting += np.dot(l0.T,l1_delta)
    #print(weighting)

def test(number):
    global weighting
    return sigmoid(np.dot(number,weighting))

y = np.array([[1,1,1,1,1]]).T

x1 = np.array([[0,1,0,0],
               [1,1,0,0],
               [0,1,0,0],
               [0,1,0,0],
               [1,1,1,0]])

x2 = np.array([[1,1,1,1],
               [0,0,0,1],
               [1,1,1,1],
               [1,0,0,0],
               [1,1,1,1]])

x3 = np.array([[1,1,1,1],
               [0,0,0,1],
               [0,1,1,1],
               [0,0,0,1],
               [1,1,1,1]])

x4 = np.array([[1,0,0,1],
               [1,0,0,1],
               [1,1,1,1],
               [0,0,0,1],
               [0,0,0,1]])

x5 = np.array([[1,1,1,1],
               [1,0,0,0],
               [1,1,1,1],
               [0,0,0,1],
               [1,1,1,1]])

x6 = np.array([[1,1,1,1],
               [1,0,0,0],
               [1,1,1,1],
               [1,0,0,1],
               [1,1,1,1]])

x7 = np.array([[0,1,1,1],
               [0,0,0,1],
               [0,0,0,1],
               [0,0,0,1],
               [0,0,0,1]])

x8 = np.array([[1,1,1,1],
               [1,0,0,1],
               [1,1,1,1],
               [1,0,0,1],
               [1,1,1,1]])

x9 = np.array([[1,1,1,1],
               [1,0,0,1],
               [1,1,1,1],
               [0,0,0,1],
               [1,1,1,1]])

x0 = np.array([[1,1,1,1],
               [1,0,0,1],
               [1,0,0,1],
               [1,0,0,1],
               [1,1,1,1]])

