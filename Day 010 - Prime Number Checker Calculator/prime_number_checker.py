def is_prime(num):
    divisor = 0
    for number in range(1, num):
        result = num % number
        if result == 0:
            divisor += 1
    if divisor == 1:
        return True
    else:
        return False
        
num = int(input("Welcome to the prime number checker. Please type your number and hit the enter key:    "))
print(is_prime(num))