MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


def process_coins():
    quarters_paid = int(input("How many quarters would you like to insert?:  "))
    dimes_paid = int(input("How many dimes would you like to insert?:  "))
    nickles_paid = int(input("How many nickles would you like to insert?:  "))
    pennies_paid = int(input("How many pennies would you like to insert?:  "))
    total_paid = ((quarters_paid * QUARTERS) + (dimes_paid * DIMES) + (nickles_paid * NICKLES) + (pennies_paid * PENNIES))
    total_paid = "{:.2f}".format(round(total_paid, 2))
    return total_paid


def dispense_coffee(u_entry, MENU, coffee_resources):
    if u_entry == "latte":
        coffee_resources["water"] -= MENU[u_entry]["ingredients"]["water"]
        coffee_resources["milk"] -= MENU[u_entry]["ingredients"]["milk"]
        coffee_resources["coffee"] -= MENU[u_entry]["ingredients"]["coffee"]
    elif u_entry == "espresso":
        coffee_resources["water"] -= MENU[u_entry]["ingredients"]["water"]
        coffee_resources["coffee"] -= MENU[u_entry]["ingredients"]["coffee"]
    else:
        coffee_resources["water"] -= MENU[u_entry]["ingredients"]["water"]
        coffee_resources["milk"] -= MENU[u_entry]["ingredients"]["milk"]
        coffee_resources["coffee"] -= MENU[u_entry]["ingredients"]["coffee"]


def refill_resources(r_values):
    refill = input("Would you like the refill the machine? Enter \"Y\" for yes or anything else to exit by entering \"report\":  ").lower()
    if refill == "y":
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100
    else:
        return


def coffee_machine(coffee_resources, MENU):
    money = 0
    coffee_machine_on = True
    while coffee_machine_on:
        user_entry = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_entry == "off":
            coffee_machine_on = False
        elif user_entry == "report":
            max = 300
            for key in resources:
                if key != "coffee":
                    print(f"{key}: {resources[key]}ml/{max}ml")
                    max -= 100
                else:
                    print(f"{key}: {resources[key]}g/{max}g")
                    max -= 100
            print(f"money: ${money}")
            refill_resources(resources)
        elif user_entry != "espresso" and user_entry != "latte" and user_entry != "cappuccino":
            print("Invalid selection")
        else:
            if coffee_resources["water"] < MENU[user_entry]["ingredients"]["water"]:
                print("Sorry there is not enough water. Check by entering \"report\".")
            elif coffee_resources["coffee"] < MENU[user_entry]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee. Check by entering \"report\".")
            elif coffee_resources["milk"] < MENU[user_entry]["ingredients"]["milk"]:
                print("Sorry there is not enough milk. Check by entering \"report\".")
            else:
                coffee_price = MENU[user_entry]['cost']
                coffee_price = "{:.2f}".format(round(coffee_price, 2))
                print(f"Please insert ${coffee_price}")
                money_inserted = float(process_coins())
                if money_inserted < MENU[user_entry]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    dispense_coffee(user_entry, MENU, coffee_resources)
                    price = MENU[user_entry]["cost"]
                    money = money + price
                    money = "{:.2f}".format(round(money, 2))
                    change = money_inserted - price
                    change = "{:.2f}".format(round(change, 2))
                    money_inserted = "{:.2f}".format(round(money_inserted, 2))
                    print(f"Total paid: ${money_inserted}. Here is your change: ${change}")
                    print(f"Enjoy your {user_entry}.")
                    money_inserted = float(money_inserted)


coffee_machine(resources, MENU)