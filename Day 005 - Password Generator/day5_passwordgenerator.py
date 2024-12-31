#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password = str("")
if nr_letters >= 1:
    for letter_choice in range(1, nr_letters + 1):
        x = random.randint(0, 51)
        alpha_character = letters[x]
        password += alpha_character

if nr_symbols >= 1:
    for symbol_choice in range(1, nr_symbols + 1):
        x = random.randint(0, 8)
        symbol_character = symbols[x]
        password += symbol_character

if nr_numbers >= 1:
    for number_choice in range(1, nr_numbers + 1):
        x = random.randint(0, 9)
        number_character = numbers[x]
        password += number_character
        
password = list(password)
random.shuffle(password)
final_password = ''.join(password)
print(f"Your new password could be:\n{final_password}")