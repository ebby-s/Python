import turtle

def koch(t, order, size,angle=120,triangle=False):
    if triangle:
        angles = [-120, -120, 0]
    else:
        angles = [angle/2, -angle, angle/2, 0]
    if order == 0:
        t.forward(size)
    else:
        for angle2 in angles:
            koch(t, order-1, size/3,angle)
            t.left(angle2)

pen = turtle.Turtle()
pen.speed(100)
pen.ht()
pen.fillcolor("black")
pen.penup()
pen.setpos(-400,200)
pen.pendown()
pen.begin_fill()
koch(pen,5,500,650,True)
pen.end_fill()
