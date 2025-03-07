from turtle import Turtle, Screen
import random
import turtle

def draw_square(turtle, side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)


def dashed_line(turtle, dash_length, total_dashes):
    for _ in range(1, total_dashes + 1):
        turtle.forward(dash_length)
        turtle.up()
        turtle.forward(dash_length)
        turtle.down()


def draw_shape(turtle, n_sides: int, length_sides):
    angle = 360 / n_sides
    while n_sides > 0:
        turtle.forward(length_sides)
        turtle.right(angle)
        n_sides -= 1


def random_color():
    """Returns a random color tuple (R, G, B) where each value is between 0 and 255."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk():
    directions = [0, 90, 180, 270]
    walk_time = random.randint(100, 300)
    for steps in range(1, walk_time + 1):
        dilbert.pencolor(random_color())
        dilbert.setheading(random.choice(directions))
        dilbert.forward(20)


def make_spirograph():
    heading = 0
    while heading < 360:
        dilbert.pencolor(random_color())
        dilbert.circle(200)
        heading += 5
        dilbert.setheading(heading)


my_screen = Screen()
my_screen.screensize (300, 300)

dilbert = Turtle("turtle")
dilbert.color("cyan")
turtle.colormode(255)
dilbert.width(4)
dilbert.speed(3)
dilbert.turtlesize(3, 3)

# dilbert.shape("turtle")

# draw_square(dilbert, 100)

# dashed_line(dilbert, 10, 10)

for sides in range(3, 11):
    dilbert.pencolor(random_color())
    draw_shape(dilbert, sides, 120)

# random_walk()

# make_spirograph()

my_screen.exitonclick()
# turtle.done()