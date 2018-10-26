import turtle
import math

colors = ["red","pink","violet","purple","blue","cyan","light green","yellow","orange"]
screen = turtle.Screen()
screen.bgcolor("black")

def line(t,angle,length): # Draws a line with an angle using the turtle
    t.right(angle)
    t.forward(length)

def draw(t,heading,length): # Draws a line with 3 parts from the center
    t.setpos([0,0])
    t.seth(heading)
    t.pendown()
    line(t,0,length)
    line(t,30,length/4)
    line(t,-30,length/2)
    t.penup()

def control(t):          # Draws lines from the center with a different angle each time, producing a circle
    for i in range(90):
        draw(t,4*i,160)


        

while __name__ == "__main__":
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.ht()
    for color in colors:
        pencil.pencolor(color)
        control(pencil)
