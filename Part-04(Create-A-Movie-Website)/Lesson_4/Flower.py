import turtle
def flower(turtle):
    window = turtle.Screen()
    window.bgcolor("coral")
    turtle = turtle.Turtle()
    turtle.speed(4)

    for i in range(10):
        for p in range(5):
            turtle.right(72)
            turtle.forward(50)
        turtle.rt(45)
    turtle.forward(250)
    turtle.backward(80)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(100)
    turtle.forward(20)
    turtle.left(99)
    turtle.forward(48)
    turtle.right(318)
    turtle.forward(90)
    turtle.hideturtle()

    window.exitonclick()

flower(turtle)
