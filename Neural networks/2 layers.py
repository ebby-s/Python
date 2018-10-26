import numpy as np
np.random.seed(1)

def sigmoid (X,deriv = False): # Sigmoid function
    if deriv == True:
        return X*(1-X)
    return 1/(1+np.exp(-X))

x = np.array([[0,1,0],
              [1,1,0],
              [1,0,1]])

w0 = 2*np.random.random((3,1))-1        # Random weights
y = np.array([[1,0,1]]).T

for i in range(10000):
    l0 = x
    l1 = sigmoid(np.dot(l0,w0))
    l1_error = y - l1
    if i%1000 == 0:
        print("l1 error: ", np.mean(np.abs(l1_error)))  # Prints error every 1000 iterations
    l1_delta = l1_error*sigmoid(l1,True)
    w0 += np.dot(l0.T,l1_delta)

print(sigmoid(np.dot(x,w0)))
