import turtle

def koch(t,order,size,angle=120):
    if order == 0:
        t.forward(size)
    else:
        for angle in [angle/2,-angle,angle/2,0]:
            koch(t,order-1,size/3,angle)
            t.left(angle)

pen = turtle.Turtle()
pen.speed(100)
pen.ht()
pen.penup()
pen.back(400)
pen.pendown()
koch(pen,5,300,100)
