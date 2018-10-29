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

def circle(t):          # Draws lines from the center with a different angle each time, producing a circle
    for i in range(90):
        draw(t,4*i,160)

def circle_with_lobes(t,lobes):     # Same as circle but the distance from the centre varies.
    for i in range(90):
        i_rads = 4*i/180*math.pi
        length = 120+20*(math.sin(i_rads*lobes)+1)
        draw(t,4*i,length)


while __name__ == "__main__":
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.ht()
    for color in colors:
        pencil.pencolor(color)
        circle_with_lobes(pencil,8)


