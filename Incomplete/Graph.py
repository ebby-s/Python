import matplotlib.pyplot as plt
import random

class Data:
    def __init__(self):
        self.data = None
        self.label = None
        self.range = None

def best_fit(X, Y):
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X)
    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2
    b = numer / denum
    a = ybar - b * xbar
    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))
    return a,b

def plot(title,X,Y):
    a,b = best_fit(X.data,Y.data)
    plt.xlabel(X.label)
    plt.ylabel(Y.label)
    plt.title(title)
    plt.scatter(X.data,Y.data)
    yfit = [a+b*xi for xi in X.data]
    plt.plot(X.data,yfit)
    plt.xlim(X.range)
    plt.ylim(Y.range)
    plt.show()
    input()

X = Data()
X.data = [0,1,1,2,4,5,7,9,11,13,15]
X.range = [0,15]
X.label = "ΔT/K"
Y = Data()
Y.data = [0,810,1610,2420,3230,4030,4840,5640,6450,7260,8060]
Y.range = [0,9000]
Y.label = "ΔQ/J"
#plot("Specific heat capacity of Cu",X,Y)

fees = Data()
fees.data = [102000,98160,130000,83880,121000]
fees.range = [0,150000]
fees.label = "fees/£"

other = Data()
other.data = [95808,48928,82200,62748,103280]
other.range = [0,150000]
other.label = "other/£"

students = Data()
students.data = [18355,15770,21550,17545,9580]
students.range = [0,25000]
students.label = "students"

plot('',fees,students)

X = [1,2,3,4,5]
Y = [146628,147088,197808,212200,224280]
X = [36657,36772,49452,42440,56070]





