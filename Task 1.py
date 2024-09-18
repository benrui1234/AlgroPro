import random
secret_number = random.randint(1, 101)
user_number = 0
user_number = int(input(print("Input your number:")))

while user_number is not secret_number:
    if user_number >= secret_number:
        print("The secret number is smaller.")
        user_number = int(input(print("Input your number:")))
    elif user_number <= secret_number:
        print("The secret number is larger.")
        user_number = int(input(print("Input your number:")))
    if user_number == secret_number:
        print("You have found the correct number!")
        break