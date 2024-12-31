fruits = ["apple", "orange", "banana"]


vegetables = ["Carrot", "celery", "broccoli"]
vegetables.append("onion")

grocery_list = [fruits]
grocery_list.extend([vegetables])

meats = ["salami", "fish", "bacon"]
grocery_list.append(meats)

last_minute_items = ["milk", "eggs"]
grocery_list.extend([last_minute_items])

print(grocery_list)