import turtle
import math
import numpy

pen = turtle.Turtle()
pencil = turtle.Turtle()
pencil.penup()

#FOR DEBUG:
pen.hideturtle()
pencil.hideturtle()
pencil.speed(100)
pen.speed(100)
'''
height = 480
width = 300
branches = 4
'''

height = numpy.random.randint(300,600)
branches = numpy.random.randint(3,5)
if branches == 3:
    whratio = numpy.random.randint(15,23)
elif branches == 4:
    whratio = numpy.random.randint(15,27)
whratio = whratio/15
width = height/whratio

def MasterMind(height,width,branches,ratio):
    pen.penup()
    pen.right(270)
    pen.forward(height/2)
    pen.right(180)
    pen.pendown()
    pen.forward(height/1.6)
    DrawBase(height/branches,width/3)
    pen.right(180)
    pen.forward(height/1.6)
    pen.right(180)
    for i in range(2,branches+2):
        DrawBranch(height/branches,width-width/i,ratio-ratio/i,i)
        pen.penup()
        pen.forward(height/branches/1.6)
        pen.pendown()
    pen.penup()
    pen.right(180)
    pen.forward(height/1.6)
    pen.right(180)
    pen.pendown()
    size = height+width
    sides = numpy.random.randint(4,6)
    DrawStar(size/branches/3,sides)

def DrawStar(size,sides):
    pen.right(180)
    tempsize = size*0.3
    pen.color("yellow")
    pen.shape("triangle")
    pen.turtlesize(size*0.06)
    for _ in range(sides):
        pen.right(360/sides)
        pen.forward(tempsize)
        pen.stamp()
        pen.backward(tempsize)

#NEW ORNAMENTS FUNCTION(INCOMPLETE):
'''
def DrawOrnaments(branchheight,width,angle,level):
    global height
    Colors = ["blue","red"]
    Shapes = ["turtle","arrow","circle"]
    temp1 = numpy.random.randint(30,branchheight-20)
    temp2 = numpy.random.randint(0,int(width/2))
    tempcolor = numpy.random.choice(Colors)
    pencil.shape(numpy.random.choice(Shapes))
    pencil.pencolor(tempcolor)
    pencil.fillcolor(tempcolor)
    pencil.setposition(0,height/2-branchheight*(level-2))
    pencil.right(90)
    pencil.forward(temp1)
    pencil.right(angle)
    pencil.forward(temp2)
    pencil.right(angle)
    pencil.stamp()
    pencil.left(angle)
    pencil.right(180)
    pencil.forward(temp2)
    pencil.right(180-angle)
'''

def DrawPresents(height,width):
    '''
    INCOMPLETE
    '''

def CalculateTriangle(height,width):
    output = []
    width2 = width/2
    output.append(180/math.pi*(math.atan(width2/height)))
    output.append(180/math.pi*(math.atan(height/width2)))
    output.append(math.sqrt((height**2)+(width2**2)))
    return output

def DrawBase(height,width):
    pen.pensize(15)
    pen.pencolor("brown")
    pen.fillcolor("brown")
    values = CalculateTriangle(height,width)
    angle1 = values[0]
    angle2 = values[1]
    hypotenuse = values[2]
    pen.right(angle1)
    pen.begin_fill()
    pen.forward(hypotenuse)
    pen.right(angle2+180)
    pen.forward(width)
    pen.right(angle2+180)
    pen.forward(hypotenuse)
    pen.end_fill()
    pen.right(180+angle1)

def DrawBranch(height,width,ratio,level):
    pen.pensize(10)
    pen.pencolor("darkgreen")
    pen.fillcolor("green")
    if level == 2:
        pen.begin_fill()
    values = CalculateTriangle(height,width)
    angle1 = values[0]
    angle2 = values[1]
    hypotenuse = values[2]
    pen.right(angle1)
    pen.penup()
    pen.forward(hypotenuse*ratio)
    pen.pendown()
    pen.begin_fill()
    pen.forward(hypotenuse*(1-ratio))
    pen.right(angle2+180)
    pen.right(30)
    for i in range(1,61):
        pen.forward(math.pi*width/3/60)
        pen.right(-1)
    pen.right(30)
    pen.right(angle2+180)
    pen.pendown()
    pen.forward(hypotenuse*(1-ratio))
    if level != 2:
        pen.end_fill()
    pen.penup()
    pen.forward(hypotenuse*ratio)
    pen.right(angle1+180)
    pen.end_fill()
    
    #FOR NEW ORNAMENTS FUNCTION:
    #DrawOrnaments(height,width,90,level)
    #DrawOrnaments(height,width,270,level)


#OLDER ORNAMENTS FUNCTION:
def DrawOrnaments(height,width,branches,angle):
    global total1
    total1 = 0
    Colors = ["blue","red"]
    Shapes = ["turtle","arrow","circle"]
    pencil.right(270)
    pencil.forward(height/2)
    pencil.right(180)
    while total1 < height-(height/branches)*2:
        temp1 = numpy.random.randint(int(height/10),int(height/branches))
        temp2 = numpy.random.randint(0,int(width/4))
        total1 += temp1
        tempcolor = numpy.random.choice(Colors)
        pencil.shape(numpy.random.choice(Shapes))
        pencil.pencolor(tempcolor)
        pencil.fillcolor(tempcolor)
        pencil.forward(temp1)
        pencil.right(angle)
        pencil.forward(temp2)
        pencil.right(angle)
        pencil.stamp()
        pencil.left(angle)
        pencil.right(180)
        pencil.forward(temp2)
        pencil.right(180-angle)
    pencil.setposition(0,0)
    pencil.left(90)

if __name__ == "__main__":
    MasterMind(height,width,branches,7/10)

    #FOR OLDER ORNAMENTS FUNCTION:
    DrawOrnaments(height,width,branches,90)
    DrawOrnaments(height,width,branches,270)


