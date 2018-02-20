import math
loop = True

def Combination():
    global C
    T = math.factorial(n)
    B1 = math.factorial(n-r)
    B2 = math.factorial(r)
    Bf = B1*B2
    C = T/Bf

while loop == True:
    a = input("a: ")
    b = input("b: ")
    n = int(input("n: "))
    Total = ""
    Tc = n + 1
    Tp = Tc

    for i in range(0,Tp,1):
        r = Tp - Tc
        Combination()
        Cs = str(int(C))
        ap = n-r
        if C > 1:
            Total = Total + Cs
        aS = str(a)
        apS = str(ap)
        A = "("+aS+")^"+apS
        As = str(A)
        if n > r:
            Total = Total + As
        bS = str(b)
        rS = str(r)
        B = "("+bS+")^"+rS
        Bs = str(B)
        if r > 0:
            Total = Total + Bs
        Tc = Tc - 1
        if Tc > 0:
            Total = Total + " + "
    print (Total)

