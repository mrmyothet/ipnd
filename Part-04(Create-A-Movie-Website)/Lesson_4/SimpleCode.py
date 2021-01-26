import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white", "green")
    brad.speed(10)

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)


def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("white","green")
    angie.speed(10)
    angie.circle(100)


def draw_triangle():
    triangle = turtle.Turtle()
    triangle.shape("turtle")
    triangle.color("white", "green")
    triangle.speed(4)

    triangle.fd(100)
    triangle.left(120)
    triangle.fd(100)
    triangle.left(120)
    triangle.fd(100)
    window.exitonclick()
draw_square()
draw_circle()
draw_triangle()
