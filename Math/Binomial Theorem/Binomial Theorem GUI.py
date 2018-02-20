import tkinter
import math
window=tkinter.Tk()
window.wm_title("Binomial theorem")

def Combination():
    global C
    T = math.factorial(n)
    B1 = math.factorial(n-r)
    B2 = math.factorial(r)
    Bf = B1*B2
    C = T/Bf

def Coefficient():
    Xt = ""
    global Fterm
    global Cterm
    global C
    
    while True:
        try:
            ValidCoeff = int(Cterm)
            break
        except ValueError:
            Cterm = str(Cterm)
            Xt = Cterm
            Xt = Xt[-1:]
            Cterm = Cterm[:-1]
            
    Coeff = ValidCoeff**pT

    if C%1 == 0:
        C = int(C)

    if C == 0:
        print("")
    elif mode == "a":
        Coeff = Coeff*C
        
    Fterm = str(Coeff) + str(Xt)
    
    if str(Xt)=="":
        print("")
    elif pT == 1:
        print("")
    else:
        Fterm = Fterm + "^" + str(pT)

def Binomial():
    global Cterm
    global pT
    global n
    global r
    global mode
    a = Myentry1.get()
    b = Myentry2.get()
    n = int(Myentry3.get())
    Terms = []
    Total = ""
    Totalp = ""
    Tc = n + 1
    Tp = Tc

    for i in range(0,Tp,1):
        Total = ""
        r = Tp - Tc
        Combination()
        Cs = str(int(C))
        ap = n-r

        if n>r:
            mode = "a"
            Cterm = a
            pT = ap
            Coefficient()
            aS = "("+str(Fterm)+")"
            Total = Total + aS
            Totalp = Totalp + aS
            mode = ""

        if r>0:
            Cterm = b
            pT = r
            Coefficient()
            bS = "("+str(Fterm)+")"
            Total = Total + bS
            Totalp = Totalp + bS

        Tc = Tc - 1
        Terms.append(Total)
        if Tc > 0:
            Totalp = Totalp + " + "
    print(Terms)
    Result1.configure (text = "Result: "+Totalp)

Instruction1 = tkinter.Label (window, text="This program uses Pascal's Triangle to expand binomials!")
Instruction1.pack()
Instruction2 = tkinter.Label (window, text = "Use (a+b)^n")
Instruction2.pack()
Instruction3 = tkinter.Label (window, text = "Then enter the values below")
Instruction3.pack()

TextA = tkinter.Label (window, text = "Type a here:")
TextA.pack()
Myentry1 = tkinter.Entry(window)
Myentry1.pack()
TextB = tkinter.Label (window, text = "Type b here:")
TextB.pack()
Myentry2 = tkinter.Entry(window)
Myentry2.pack()
TextC = tkinter.Label (window, text = "Type n here:")
TextC.pack()
Myentry3 = tkinter.Entry(window)
#Myentry3.bind("<Return>", Binomial)
Myentry3.pack()

Button1 = tkinter.Button(window, text="Expand", command=Binomial)
Button1.pack()


Spacer1 = tkinter.Label (window, text = "")
Spacer1.pack()

Result1 = tkinter.Label(window, text="Result:")
Result1.pack()

Spacer2 = tkinter.Label (window, text = "")
Spacer2.pack()

window.mainloop()
