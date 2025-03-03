from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
line_position = 100

# def turtle_naming(d_turtle):
#     for number in range(6):
#         d_turtle = colors[number]
#         print(d_turtle)
#     return d_turtle


for number in range(6):
    d = Turtle(shape="turtle")
    d.color(f"{colors[number]}")
    d.penup()
    d.goto(x=-230, y=line_position)
    line_position -= 40

my_screen.exitonclick()