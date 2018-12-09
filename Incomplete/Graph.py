import matplotlib.pyplot as plt

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

X = [0,1,1,2,4,5,7,9,11,13,15]
Y = [0,810,1610,2420,3230,4030,4840,5640,6450,7260,8060]
a, b = best_fit(X, Y)

plt.xlabel('ΔT/K')
plt.ylabel('ΔQ/J')
plt.title('Specific heat capacity of Cu')
plt.scatter(X, Y)
yfit = [a + b * xi for xi in X]
plt.plot(X, yfit)
plt.show()
input()



