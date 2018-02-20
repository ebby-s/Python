import tkinter
import math
window = tkinter.Tk()
window.wm_title("Quadratic formula")

def QuadraticFormula():
    global a
    global b
    global c
    a = float(Myentry1.get())
    b = float(Myentry2.get())
    c = float(Myentry3.get())
    D = b**2 - 4*a*c
    T = -b + D**0.5
    OT = -b - D**0.5
    B = 2*a
    X1 = T/B
    X2 = OT/B
    iX1 = -X1
    iX2 = -X2
    c_mult = c/(iX1*iX2)
    miX1 = iX1*c_mult
    miX2 = iX2*c_mult
    Tb = b/2
    Tb2 = Tb**2
    Tp = c - Tb2
    Ra = math.sqrt(a)
    Tpxi = Tb2/Ra
    Tpx = -Tpxi
    if D > 0:
        Roots = "2"
    elif D == 0:
        Roots = "1"
    else:
        Roots = "0"

    Result1.configure (text = "X1 = " + str(X1))
    Result2.configure (text = "X2 = " + str(X2))
    Result3.configure (text = "Discriminant = " + str(D))
    Result4.configure (text = "Roots (Number of intersetions with X-axis) : " + Roots)
    Result5.configure (text = "Turning point: (" + str(Tpx) + "," + str(Tp) + ")")

def Edity(Edit):
    a = float(Myentry1.get())
    b = float(Myentry2.get())
    c = float(Myentry3.get())
    yedit = float(Edit1.get())
    c += yedit
    D = b**2 - 4*a*c
    T = -b + D**0.5
    OT = -b - D**0.5
    B = 2*a
    X1 = T/B
    X2 = OT/B
    iX1 = -X1
    iX2 = -X2
    if D > 0:
        Roots = "2"
    elif D == 0:
        Roots = "1"
    else:
        Roots = "0"
    Result1.configure (text = "X1 = " + str(X1))
    Result2.configure (text = "X2 = " + str(X2))
    Result3.configure (text = "Discriminant = " + str(D))
    Result4.configure (text = "Roots (Number of intersetions with X-axis) : " + Roots)
    Result5.configure (text = "Factorised : (X+" + str(iX1) + ")(X+" + str(iX2) + ") = 0")

def Editx(Edit):
    a = float(Myentry1.get())
    b = float(Myentry2.get())
    c = float(Myentry3.get())
    xedit = float(Edit2.get())
    D = b**2 - 4*a*c
    T = -b + D**0.5
    OT = -b - D**0.5
    B = 2*a
    X1 = T/B + xedit
    X2 = OT/B + xedit
    iX1 = -X1
    iX2 = -X2
    if D > 0:
        Roots = "2"
    elif D == 0:
        Roots = "1"
    else:
        Roots = "0"
    Result1.configure (text = "X1 = " + str(X1))
    Result2.configure (text = "X2 = " + str(X2))
    Result3.configure (text = "Discriminant = " + str(D))
    Result4.configure (text = "Roots (Number of intersetions with X-axis) : " + Roots)
    Result5.configure (text = "Factorised : (X+" + str(iX1) + ")(X+" + str(iX2) + ") = 0")

Instruction1 = tkinter.Label (window, text="This program uses Quadratic Formula to find values of X and more!")
Instruction1.pack()
Instruction2 = tkinter.Label (window, text = "First, solve for an equation in the form of AX^2+BX+C=0")
Instruction2.pack()
Instruction3 = tkinter.Label (window, text = "Then enter the values below")
Instruction3.pack()

TextA = tkinter.Label (window, text = "Type A here:")
TextA.pack()
Myentry1 = tkinter.Entry(window)
Myentry1.pack()
TextB = tkinter.Label (window, text = "Type B here:")
TextB.pack()
Myentry2 = tkinter.Entry(window)
Myentry2.pack()
TextC = tkinter.Label (window, text = "Type C here:")
TextC.pack()
Myentry3 = tkinter.Entry(window)
Myentry3.pack()

Button2 = tkinter.Button(window, text="Calculate", command=QuadraticFormula)
Button2.pack()

Result1 = tkinter.Label(window, text="X1 = ")
Result1.pack()
Result2 = tkinter.Label(window, text="X2 = ")
Result2.pack()
Result3 = tkinter.Label(window, text="Discriminant: ")
Result3.pack()
Result4 = tkinter.Label(window, text="Roots (Number of intersetions with X-axis): ")
Result4.pack()
Result5 = tkinter.Label(window, text="Turning point: ")
Result5.pack()

EditInstruction1 = tkinter.Label(window, text="Move Max/Min point on Y-axis:")
EditInstruction1.pack()
Edit1 = tkinter.Entry(window)
Edit1.bind("<Return>", Edity)
Edit1.pack()
EditInstruction2 = tkinter.Label(window, text="Move Max/Min point on X-axis:")
EditInstruction2.pack()
Edit2 = tkinter.Entry(window)
Edit2.bind("<Return>", Editx)
Edit2.pack()

window.mainloop()
