from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
my_screen.title("Press the \"spacebar\" to start the race")
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
line_position = 100
ALL_TURTLES = []

if user_bet:
    is_race_on = True


# def race_setup(a_turtles, l_position):
for number in range(6):
    d = Turtle(shape="turtle")
    turtle_name = colors[number]
    d.color(turtle_name)
    d.penup()
    d.goto(x=-230, y=line_position)
    ALL_TURTLES.append(d)
    line_position -= 40


def race():
    global is_race_on
    while is_race_on:
        # mover = random.choice(ALL_TURTLES)
        for turtle in ALL_TURTLES:
            distance = random.randint(0,10)
            turtle.forward(distance)
            finish_line = 230
            turtle_position = turtle.xcor()
            if turtle_position >= finish_line:
                is_race_on = False
                if user_bet == turtle.pencolor():
                    print(f"You have won the bet! The {turtle.pencolor()} turtle won the race.")
                else: 
                    print(f"The {turtle.pencolor()} turtle won the race. You have lost.")


my_screen.listen()
my_screen.onkey(key="space", fun=race)





my_screen.exitonclick()