import turtle
import math

valid = False
while not valid:
    print("""Choose a speed:
    1. For testing purposes only (90)
    2. Low quality (180)
    3. Meh quality (360)
    4. Good quality (720)
    5. Will be done by tomorrow, I think (1080)""")
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        if 0 < choice < 6:
            valid = True
        else:
            print("That isn't an opition lol...")
    except ValueError:
        print("Thats not a valid choice you monkey...")

if choice == 1:
    time = 90
elif choice == 2:
    time = 180
elif choice == 3:
    time = 360
elif choice == 4:
    time = 720
elif choice == 5:
    time = 1080

valid = False
while not valid:
    print("""Choose a speed:
    1. Tiny sized (0.6)
    2. Laptop size (0.8)
    3. Normal size (1)
    4. The bigger, blacker version (1.2)""")
    choice = input("Your choice: ")
    try:
        choice = int(choice)
        if 0 < choice < 5:
            valid = True
        else:
            print("That isn't even an opition...")
    except ValueError:
        print("Thats not a valid choice you gremlin...")

if choice == 1:
    size = 0.6
elif choice == 2:
    size = 0.8
elif choice == 3:
    size = 1
elif choice == 4:
    size = 1.2

wn = turtle.Screen()
pen = turtle.Turtle()
pencil = turtle.Turtle()
pen.penup()
pencil.penup()
pen.ht()
pencil.ht()
pen.speed(100)
pencil.speed(100)
turtle.bgcolor("#0060ff")

def Flower(pos,size,thickness,colors,control=2.2,shape=32,density=720,shape2="narrow",number=5,angles=[30,30]):
    for j in range(number+1):
        pencil.seth(-360/number*j)
        number2 = number
        if j == number:
            pencil.seth(0)
            number2 = number*1.5
        Pattern(shape2,pos,size,thickness,colors,shape,density,control,angles,[1,0.2,0.5],number2)

def Pattern(shape,pos,size,thickness,lcolors,depth=1,density=900,blobs=4,langles=[30,30],lratios=[1,0.2,0.5],parts=1):
    pencil.pensize(thickness)
    pencil.setpos(pos)
    pencil.pendown()
    blobs = density/blobs/2
    for i in range(int(density/parts)):
        pencil.pencolor(lcolors[0])
        dmult = density/blobs/depth
        mult = (function(i,blobs,shape)+dmult)/(1+dmult)
        pencil.forward(size*mult*lratios[0])
        pencil.pencolor(lcolors[1])
        pencil.right(langles[0])
        pencil.forward(size*mult*lratios[1])
        pencil.pencolor(lcolors[2])
        pencil.left(langles[0]+langles[1])
        pencil.forward(size*mult*lratios[2])
        pencil.right(langles[1]+360/density)
        pencil.penup()
        pencil.setpos(pos)
        pencil.pendown()
    pencil.penup()

def function(ival,blobs,shape):
    val = math.sin(ival/blobs*math.pi)
    if shape == "broad":
        return 2*val-val**2
    else:
        return val

def start(angle,pos,color,pensize):
    pen.penup()
    pen.setpos(pos)
    pen.seth(angle)
    pen.pensize(pensize)
    pen.pencolor(color)
    pen.pendown()

def a(size,pos,color,pensize):
    pos = [pos[0],pos[1]+size*0.6]
    size = size*0.8
    start(0,pos,color,pensize)
    pen.forward(size*0.1)
    for i in range(125):
        pen.forward(size/200)
        pen.right(math.sin(i/50))
    pen.forward(size*0.05)
    lstart = pen.pos()
    for i in range(80):
        pen.forward(size/200)
        pen.left(math.sin(i/50))
    pen.penup()
    pen.setpos(lstart)
    pen.seth(270)
    pen.forward(size*0.1)
    pen.left(10)
    pen.pendown()
    for i in range(180):
        rads = i/90*math.pi
        pen.forward((size*(math.sin(rads)**2)**0.5+size*0.4)/(115))
        pen.right(2)

def B(size,pos,color,pensize):
    start(90,pos,color,pensize)
    pen.forward(size)
    pen.right(90)
    pen.forward(size*0.2)
    for i in range(90):
        pen.forward(size*0.007854)
        pen.right(2)
    pen.forward(size*0.2)
    pen.right(180)
    pen.forward(size*0.25)
    for i in range(90):
        pen.forward(size*0.0096)
        pen.right(2)
    pen.forward(size*0.25)

def c(size,pos,color,pensize):
    pos = [pos[0],pos[1]+size*0.529]
    start(150,pos,color,pensize)
    for i in range(60):
        pen.forward(size/50)
        pen.left(4)

def M(size,pos,color,pensize):
    start(80,pos,color,pensize)
    pen.forward(size)
    pen.right(140)
    pen.forward(size*0.8)
    pen.left(120)
    pen.forward(size*0.8)
    pen.right(140)
    pen.forward(size)
    pen.penup()

def d(size,pos,color,pensize):
    pos = [pos[0]+size*0.529,pos[1]]
    start(90,pos,color,pensize)
    pen.forward(size)
    pen.setpos(pos[0],pos[1]+size*0.3)
    pen.right(180)
    for i in range(180):
        pen.forward(size*0.0105)
        pen.right(2)

def h(size,pos,color,pensize):
    start(90,pos,color,pensize)
    pen.forward(size)
    pen.setpos(pos[0],pos[1]+size*0.3)
    for i in range(90):
        pen.forward(size*0.0105)
        pen.right(2)
    pen.forward(size*0.3)

def H(size,pos,color,pensize):
    start(90,pos,color,pensize)
    pen.forward(size)
    pen.right(180)
    pen.forward(size*0.5)
    pen.left(90)
    pen.forward(size*0.5)
    pen.right(90)
    pen.forward(size*0.5)
    pen.right(180)
    pen.forward(size)

def i(size,pos,color,pensize,shape):
    pen.shape(shape)
    start(90,pos,color,pensize)
    pen.forward(size*0.6)
    pen.penup()
    pen.forward(size*0.2)
    pen.stamp()

def p(size,pos,color,pensize):
    pos = [pos[0],pos[1]-size*0.4]
    start(90,pos,color,pensize)
    pen.forward(size)
    pen.setpos(pos[0],pos[1]+size*0.7)
    for i in range(180):
        pen.forward(size*0.0105)
        pen.right(2)
    
def r(size,pos,color,pensize):
    start(90,pos,color,pensize)
    pen.forward(size*0.6)
    pen.setpos(pos[0],pos[1]+size*0.3)
    for i in range(45):
        pen.forward(math.sin(i/20)*size/75)
        pen.right(2)
    
def t(size,pos,color,pensize):
    pos = [pos[0]+size*0.2,pos[1]+size]
    start(270,pos,color,pensize)
    pen.forward(size*0.8)
    for i in range(80):
        pen.forward(size*0.007)
        pen.left(2)
    pen.penup()
    pen.setpos(pos[0]-size*0.15,pos[1]-size*0.3)
    pen.seth(0)
    pen.pendown()
    pen.forward(size*0.5)

def y(size,pos,color,pensize):
    pos = [pos[0],pos[1]+size*0.6]
    start(270,pos,color,pensize)
    pen.forward(size*0.2)
    for i in range(90):
        pen.forward(size*0.0105)
        pen.left(2)
    pen.forward(size*0.2)
    pen.seth(270)
    pen.forward(size*0.8)
    for i in range(85):
        pen.forward(size*0.0105)
        pen.right(2)

Pattern("broad",[-20*size,40*size],250*size,1,["#0060ff","#dbd1b4","#3fe0d0"],0.25,1.5*time)
Pattern("narrow",[380*size,290*size],65*size,1,["green","green","green"],6,time,3)
Pattern("narrow",[-400*size,360*size],65*size,1,["green","green","green"],6,time,3)
Flower([380*size,290*size],50*size,1,["#3fe0d0","#7fffd4","white"],2.17,32,time,"narrow",5,[30,30])
Flower([-420*size,-210*size],50*size,1,["yellow","orange","red"],2.17,32,time,"narrow",5,[30,30])
Flower([360*size,-280*size],50*size,1,["magenta","#ff0024","darkred"],2.17,32,time,"broad",5,[30,30])
Flower([-400*size,360*size],50*size,1,["#7fffd4","lightblue","white"],2.17,32,time,"broad",5,[30,30])
a(70*size,[-100*size,120*size],"#7fffd4",5)
a(70*size,[80*size,0],"#7fffd4",5)
a(70*size,[20*size,-100*size],"#7fffd4",5)
B(70*size,[-200*size,0],"#7fffd4",5)
c(70*size,[0,-100*size],"#7fffd4",5)
d(70*size,[20*size,0],"#7fffd4",5)
H(70*size,[-150*size,120*size],"#7fffd4",5)
h(70*size,[-40*size,0],"#7fffd4",5)
i(70*size,[-150*size,0],"#7fffd4",5,"turtle")
i(70*size,[-50*size,-100*size],"#7fffd4",5,"turtle")
M(70*size,[-150*size,-100*size],"#7fffd4",5)
p(70*size,[-50*size,120*size],"#7fffd4",5)
p(70*size,[10*size,120*size],"#7fffd4",5)
r(70*size,[-130*size,0],"#7fffd4",5)
t(70*size,[-100*size,0],"#7fffd4",5)
y(70*size,[70*size,120*size],"#7fffd4",5)
y(70*size,[130*size,0],"#7fffd4",5)

wn.mainloop()
