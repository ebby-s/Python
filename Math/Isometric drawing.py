import turtle
turtle.setup(800,450)
d = turtle.Screen()
d.title("I'm bored...")
d.bgcolor("black")
pen = turtle.Turtle()
pen.pensize(10)
pen.pencolor("red")
pen.speed(100)
pen.left(90)

def show():
    pen.penup()

def hide():
    pen.pendown()

def forward():
    if pen.heading()%90 == 0:
        pen.forward(10)
    else:
        pen.forward(20)
    
def back():
    if pen.heading()%90 == 0:
        pen.forward(-10)
    else:
        pen.forward(-20)

def left():
    pen.left(30)

def right():
    pen.right(30)

def erase():
    pen.pencolor("black")

def write():
    pen.pencolor("red")

d.onkey(show,"q")
d.onkey(hide,"e")
d.onkey(forward,"w")
d.onkey(back,"s")
d.onkey(right,"d")
d.onkey(left,"a")
d.onkey(erase,"x")
d.onkey(write,"c")

d.listen()
d.mainloop()
