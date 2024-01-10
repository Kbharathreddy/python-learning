import turtle
turtle.bgcolor("white")

squary=turtle.Turtle()
squary1=turtle.Turtle()
squary.speed(10)
squary1.speed(10)
squary.pencolor("red")
squary1.pencolor("blue")
for i in range(800):
    squary.forward(i)
    squary.right(62)
    squary1.forward(i)
    squary1.left(62)
