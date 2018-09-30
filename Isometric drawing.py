import turtle
turtle.setup(800,450)
screen = turtle.Screen()
screen.title("I'm bored...")
screen.bgcolor("black")
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

screen.onkey(forward,"w")
screen.onkey(left,"a")
screen.onkey(back,"s")
screen.onkey(right,"d")
screen.onkey(show,"q")
screen.onkey(hide,"e")
screen.onkey(erase,"x")
screen.onkey(write,"c")

screen.listen()
screen.mainloop()
