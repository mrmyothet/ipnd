import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(third_turtle):
    for i in range(1,4):
        third_turtle.forward(100)
        third_turtle.left(120)

def draw_art():
    window = turtle.Screen()
    turtle.bgcolor("indianred")
# Create the turtle brad -- Draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "green")
    brad.speed(4)
    draw_square(brad)

# Create the turtle angie -- Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.speed(2)
    angie.circle(100)

# Create the turtle triangle -- Draws a triangle

    triangle = turtle.Turtle()
    triangle.shape("arrow")
    triangle.color("white")
    triangle.speed(2)
    draw_triangle(triangle)

    window.exitonclick()
draw_art()
