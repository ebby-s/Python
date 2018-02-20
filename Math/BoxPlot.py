import turtle
outliers = []

def get_data():
    global minv
    global maxv
    global Q1
    global Q2
    global Q3
    minv = int(input("Min value:"))
    maxv = int(input("Max value:"))
    Q1 = int(input("Lower quartile:"))
    Q2 = int(input("Median:"))
    Q3 = int(input("Upper quartile:"))

def calc_outliers():
    global outliers
    global Q1
    global Q3
    global lowout
    global upout
    outrange = 1.5*(Q3-Q1)
    lowout = Q1-outrange
    upout = Q3+outrange
    outnum = int(input("How many outliers would you like to enter? "))
    for i in range(0,outnum,1):
        temp = int(input("Enter outlier:"))
        outliers.append(temp)

def prep_data():
    global minv
    global maxv
    global Q1
    global Q2
    global Q3
    global len1
    global len2
    global len3
    global len4
    global lowout
    global upout
    global outlowlen
    global outuplen
    mult = 500/maxv
    outlowlen = mult*(lowout-minv)
    outuplen = mult*(upout-minv)
    minv = mult*minv
    maxv = mult*maxv
    Q1 = mult*Q1
    Q2 = mult*Q2
    Q3 = mult*Q3
    len1 = Q1 - minv
    len2 = Q2 - Q1
    len3 = Q3 - Q2
    len4 = maxv - Q3

def line_perpendicular(turtle,length):
    turtle.right(90)
    turtle.forward(length)
    turtle.left(180)
    turtle.forward(2*length)
    turtle.right(180)
    turtle.forward(length)
    turtle.left(90)

def line_parallel(length):
    pen.forward(length)
    pen.right(180)
    pen.forward(length)
    pen.right(180)

get_data()
calc_outliers()
prep_data()

wn = turtle.Screen()
pen = turtle.Turtle()
outpen = turtle.Turtle()

pen.penup()
pen.right(180)
pen.forward(300)
pen.right(180)
pen.pendown()
outpen.penup()
outpen.right(180)
outpen.forward(300)
outpen.right(180)
outpen.pendown()

if minv < lowout:
    outpen.forward(outlowlen)
    line_perpendicular(outpen,20)
    outpen.right(180)
    outpen.forward(outlowlen)
    outpen.right(180)

if maxv > upout:
    outpen.penup()
    outpen.forward(outuplen)
    outpen.pendown()
    line_perpendicular(outpen,20)
    outpen.penup()
    outpen.right(180)
    outpen.forward(outuplen)
    outpen.right(180)
    outpen.pendown()

line_perpendicular(pen,25)
pen.forward(len1)

line_perpendicular(pen,25)
pen.right(90)
pen.forward(25)
pen.left(90)
line_parallel(len2)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(len2)
pen.right(90)
pen.forward(50)
pen.left(90)
line_parallel(len3)
pen.left(90)
pen.forward(50)
pen.right(90)
pen.forward(len3)
pen.right(90)
pen.forward(50)
pen.right(180)
pen.forward(25)
pen.right(90)

pen.forward(len4)
line_perpendicular(pen,25)
print(outlowlen)
print(outuplen)
print(upout)
print(lowout)
wn.mainloop()
