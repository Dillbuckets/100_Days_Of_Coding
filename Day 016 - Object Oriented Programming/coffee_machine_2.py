from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

def run_report():
    money_machine.report()
    coffee_maker.report()

while is_on:
    selections = menu.get_items()
    user_choice = input(f"What would you like? Choose from the following {selections}:\n").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        run_report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

