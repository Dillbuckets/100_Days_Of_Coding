a = 100
b = 200
user_guess = input("Which number is larger? Type \"a\" for A or \"b\" for b:  ").lower()

def compare(a, b, user_guess):
    if a > b:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
print(compare(a, b, user_guess))