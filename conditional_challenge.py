import random
random_number = random.randint(1, 10)
current_guess = random.randint(1, 10)

if current_guess != random_number:
    print("I didn't find the number :(")
else:
    print("I found the number!! Yippeee!!!")
