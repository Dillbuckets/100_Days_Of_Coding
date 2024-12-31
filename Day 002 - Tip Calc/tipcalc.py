print("Welcome to the tip calculator!")
bill_total = float(input("What was the total of the bill?\n $"))
tip_amount = int(input("What percentage tip would you like to give? Examples: \"15\", \"20\", \"22\"\n"))
tip_percent = tip_amount * 0.01
total_paying = int(input("How many people are splitting this bill?\n"))
tip_total = bill_total * tip_percent
grand_total = bill_total + tip_total
each_pays = grand_total / total_paying
final_amounts = "{:.2f}".format(round(each_pays, 2))
print(f"The amount each person should pay is: ${final_amounts}")