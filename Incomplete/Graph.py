import matplotlib.pyplot as plt

X = [0,1,1,2,4,5,7,9,11,13,15]
Y = [0,810,1610,2420,3230,4030,4840,5640,6450,7260,8060]

def best_fit(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = numer / denum
    a = ybar - b * xbar
    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))
    return a, b

a, b = best_fit(X, Y)

plt.scatter(X, Y)
yfit = [a + b * xi for xi in X]
plt.plot(X, yfit)
plt.show()

'''
import scipy.optimize as optimization
import numpy

def func(x,a,b):
    return a+b*x

xs = numpy.array([0,1,1,2,4,5,7,9,11,13,15])
ys = numpy.array([0,810,1610,2420,3230,4030,4840,5440,6450,7260,8060])
x0    = numpy.array([0.0, 0.0, 0.0])
sigma = numpy.array([1.0,1.0,1.0,1.0,1.0,1.0])

plt.xlabel('Change in T')
plt.ylabel('Change in Q')
plt.plot(xs,ys, 'ro')
plt.axis([0, 16, 0, 8500])

x = numpy.linspace(0,16,100)
y = 430*x+1600
plt.plot(x, y, '-r', label='y=2x+1')

plt.show()
#print(optimization.curve_fit(func, xs, ys, x0, sigma))
input()
'''
