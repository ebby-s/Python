import numpy as np
np.random.seed(1)

def sigmoid (X,deriv = False): # Sigmoid function
    if deriv == True:
        return X*(1-X)
    return 1/(1+np.exp(-X))

x = np.array([[0,1,0],
              [1,1,0],
              [1,0,1],
              [1,1,1]])

y = np.array([[1,0,1,0]]).T

w0 = 2*np.random.random((3,4))-1      # Random weights
w1 = 2*np.random.random((4,1))-1

for i in range(20000):
    l0 = x
    l1 = sigmoid(np.dot(l0,w0))
    l2 = sigmoid(np.dot(l1,w1))

    l2_error = y - l2
    l2_delta = l2_error*sigmoid(l2,True)
    
    l1_error = np.dot(l2_delta,w1.T)
    l1_delta = l1_error*sigmoid(l1,True)
    
    w0 += np.dot(l0.T,l1_delta)
    w1 += np.dot(l1.T,l2_delta)
    if i%5000 == 0:
        print("l1 error: ", np.mean(np.abs(l1_error)))  # Prints error from the layers every 5000 iterations
        print("l2 error: ", np.mean(np.abs(l2_error)))

l1 = sigmoid(np.dot(l0,w0))
print(sigmoid(np.dot(l1,w1)))
