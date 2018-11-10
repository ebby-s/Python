import tkinter
from tkinter import *
window = tkinter.Tk()
window.wm_title("Calculator with better layout")
M = int(0)
S = ""
V1 = "0"
V2 = "0"
R = ""
Number = "V1"

def N1():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "1"
    elif Number == "V2":
        V2 = V2 + "1"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N2():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "2"
    elif Number == "V2":
        V2 = V2 + "2"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N3():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "3"
    elif Number == "V2":
        V2 = V2 + "3"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N4():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "4"
    elif Number == "V2":
        V2 = V2 + "4"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N5():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "5"
    elif Number == "V2":
        V2 = V2 + "5"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N6():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "6"
    elif Number == "V2":
        V2 = V2 + "6"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N7():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "7"
    elif Number == "V2":
        V2 = V2 + "7"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N8():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "8"
    elif Number == "V2":
        V2 = V2 + "8"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N9():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "9"
    elif Number == "V2":
        V2 = V2 + "9"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def N0():
    global V1
    global V2
    if Number == "V1":
        V1 = V1 + "0"
    elif Number == "V2":
        V2 = V2 + "0"
    Value1.configure (text= V1)
    Value2.configure (text= V2)

def Add():
    global Number
    global S
    S = "+"
    Number = "V2"
    Sign.configure(text= S)

def Subtract():
    global Number
    global S
    S = "-"
    Number = "V2"
    Sign.configure(text= S)

def Multiply():
    global Number
    global S
    S = "*"
    Number = "V2"
    Sign.configure(text= S)

def Divide():
    global Number
    global S
    S = "/"
    Number = "V2"
    Sign.configure(text= S)

def E():
    global Number
    global V1
    global V2
    global R
    V1 = int(V1)
    V2 = int(V2)
    Number = "V1"
    if S == "+":
        R = V1 + V2
    elif S == "-":
        R = V1 - V2
    elif S == "*":
        R = V1 * V2
    elif S == "/" and V2 != 0:
        R = V1 / V2
    elif V2 == 0:
        R = "Division by 0"
    Result.configure(text= R)
    V1 = "0"
    V2 = "0"

def C():
    V1 = "0"
    V2 = "0"
    Value1.configure (text= V1)
    Value2.configure (text= V2)



MyTitle = tkinter.Label(window, text="Calculator",font="Helvetica 16 bold")
MyTitle.pack()
Value1 = tkinter.Label(window, text= V1, font="Helvetica 13" )
Value1.pack()
Sign = tkinter.Label(window, text= S, font="Helvetica 13" )
Sign.pack()
Value2 = tkinter.Label(window, text= V2, font="Helvetica 13" )
Value2.pack()
Result = tkinter.Label(window, text= R, font="Helvetica 13" )
Result.pack()

Button1 = tkinter.Button(window, text=" 1 ", command=N1)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 2 ", command=N2)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 3 ", command=N3)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 4 ", command=N4)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" 5 ", command=N5)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" 6 ", command=N6)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 7 ", command=N7)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 8 ", command=N8)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" 9 ", command=N9)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" 0 ", command=N0)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" + ", command=Add)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" - ", command=Subtract)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" * ", command=Multiply)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
Button1 = tkinter.Button(window, text=" / ", command=Divide)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" = ", command=E)
Button1.pack(ipadx=18,ipady=6)
Button1 = tkinter.Button(window, text=" C ", command=C)
Button1.pack(ipadx=18,ipady=6,side=LEFT)
window.mainloop()
