import turtle

def draw_flower(turtle):
    turtle.left(30)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(50)
    turtle.right(150)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")

    brad = turtle.Turtle()
    brad.speed(5)
    brad.shape("arrow")
    brad.color("yellow")

    for i in range(0,36):
        draw_flower(brad)
        brad.right(10)
    brad.color("green")
    brad.right(90)
    brad.forward(250)
    brad.backward(50)
    brad.left(120)
    brad.forward(50)
    brad.left(75)
    brad.forward(20)
    brad.right(235)
    brad.forward(55)

    brad.hideturtle()
    window.exitonclick()
draw_art()
