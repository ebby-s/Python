import turtle

colors = ["red","pink","violet","purple","blue","cyan","light green","yellow","orange"]
screen = turtle.Screen()
screen.bgcolor("black")

def draw(color):
    pencil = turtle.Turtle()
    pencil.speed(100)
    pencil.ht()
    pencil.pencolor(color)
    for i in range(45):
        pencil.pendown()
        pencil.forward(200)
        pencil.right(30)
        pencil.forward(80)
        pencil.penup()
        pencil.setpos([0,0])
        pencil.seth(8*(1+i))

while __name__ == "__main__":
    for color in colors:
        draw(color)
