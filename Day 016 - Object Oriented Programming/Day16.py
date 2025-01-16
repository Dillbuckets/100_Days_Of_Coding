# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)

# my_screen = Screen()
# my_screen.screensize(100, 100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Names", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Names"] = "r"
table.align["Type"] = "l"
print(table)