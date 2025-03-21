from turtle import Screen
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(height=600,width=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()

# segments = [1, 2, 3]
# starting_position = 0
# snake_length = []



game_continue = True
while game_continue:
    my_screen.update()
    time.sleep(0.1)
    my_screen.listen()
    my_screen.onkey(key="w", fun=up)
    # game_continue = check_walls(s_length, game_continue)






my_screen.update()

my_screen.listen()
my_screen.onkey(key="w", fun=up)
# my_screen.onkey(key="s", fun=turn_down)
# my_screen.onkey(key="a", fun=turn_left)
# my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="space", fun=beginning_snake)








my_screen.exitonclick()