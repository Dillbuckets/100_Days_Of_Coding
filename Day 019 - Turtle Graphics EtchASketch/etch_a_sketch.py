from turtle import Turtle, Screen

d = Turtle()
my_screen = Screen()


def move_forwards():
    d.forward(10)


def move_backwards():
    d.backward(10)


def turn_left():
    new_heading = d.heading() + 10
    d.setheading(new_heading)


def turn_right():
    new_heading = d.heading() - 10
    d.setheading(new_heading)


def clear():
    d.clear()
    d.up()
    d.home()
    d.down()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="c", fun=clear)
my_screen.exitonclick()