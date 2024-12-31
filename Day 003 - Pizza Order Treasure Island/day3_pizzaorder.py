pizza_size = input("What size pizza would you like? Select \"S\", \"M\", or \"L\":  ").lower()
pepperoni_topping = input("Would you like pepperoni on your pizza? Select \"Y\" for yes or \"N\": ").lower()
extra_cheese = input("Would you like extra cheese on your pizza? Select \"Y\" for yes or \"N\": : ").lower()
pizza_price = 0
order = True
incorrect_answers = 0

if pizza_size == "s":
    pizza_price += 15
elif pizza_size == "m":
    pizza_price += 20
elif pizza_size == "l":
    pizza_price += 25
else:
    order = False
    incorrect_answers += 1
    print("You have made in invalid selection.")

if pepperoni_topping == "y" and pizza_size == "s":
    pizza_price += 2
elif pepperoni_topping == "y" and pizza_size != "s":
    pizza_price += 3
elif pepperoni_topping == "n":
    print("No pepperoni selected.")
else:
    order = False
    incorrect_answers += 1
    print("Invalid selection. Must choose either y or n.")

if extra_cheese == "y":
    pizza_price += 1
elif extra_cheese == "n":
    print("Hold the extra cheese.")
else:
    order = False
    incorrect_answers += 1
    print("Invalid selection. Must choose either y or n.")

if order:
    print(f"The cost of your pizza is ${pizza_price}")
elif not order:
    if incorrect_answers < 3:
        print("No pizza for you!")
    else:
        print("You are too dumb to eat pizza. Eat crayons instead!")
