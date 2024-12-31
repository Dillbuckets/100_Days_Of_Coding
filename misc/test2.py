MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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





def coffee_machine(coffee_resources, MENU):
    coffee_machine_on = True
    while coffee_machine_on:
        user_entry = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_entry == "off":
            coffee_machine_on = False
        elif user_entry == "report":
            max = 300
            for key in resources:
                print(f"{key}: {resources[key]}/{max}")
                max -= 100
        else:
            if coffee_resources["water"] < MENU[user_entry]["ingredients"]["water"]:
                print("Sorry there is not enough water")
            elif coffee_resources["milk"] < MENU[user_entry]["ingredients"]["milk"]:
                print("Sorry there is not enough milk")
            elif coffee_resources["coffee"] < MENU[user_entry]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee")
            else:
                print(f"Please insert ${MENU[user_entry]['cost']}")
                money_inserted = float(process_coins())
                if money_inserted < MENU[user_entry]["cost"]:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    dispense_coffee(user_entry, MENU, coffee_resources)
                    change = money_inserted - MENU[user_entry]["cost"]
                    print(f"Here is your change: ${change}")



coffee_machine(resources, MENU)
           



# print report with remaining resource values
# when user imput for item selection, can enter "report" to see values including money
# check if resources are sufficient to produce a product being ordered
# process coins by asking the quantity of each coin type
# calculate if there is enough money and determine success of transaction
# determine change