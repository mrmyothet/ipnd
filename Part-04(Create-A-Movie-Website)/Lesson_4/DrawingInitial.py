import turtle

def draw_myname():
    window = turtle.Screen()
    window.bgcolor("white")

    name = turtle.Turtle()
    name.rt(90)
    name.fd(120)
    name.backward(60)
    name.left(130)
    name.forward(90)
    name.backward(90)
    name.left(280)
    name.forward(90)
    name.right(320)
    name.fd(90)
    name.backward(90)
    name.left(90)
    name.fd(115)
    name.left(270)
    name.fd(90)
    name.right(90)
    name.fd(115)
    name.right(270)
    name.forward(90)

    window.exitonclick()
draw_myname()
