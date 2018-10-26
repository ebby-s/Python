loop = True
while loop == True:
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    D = b**2 - 4*a*c
    T = -b + D**0.5
    OT = -b - D**0.5
    B = 2*a
    X1 = T/B
    X2 = OT/B
    if D > 0:
        Roots = "2"
    elif D == 0:
        Roots = "1"
    else:
        Roots = "0"
    print ("X1 = " + str(X1))
    print("X2 = " + str(X2))
    print("Discriminant = " + str(D))
    print("Roots (Number of intersetions with X-axis) : " + Roots)
