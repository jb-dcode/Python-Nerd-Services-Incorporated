import random

min = -29389518293123
max = 92301239132060

random_number = random.randint(min, max)

current_guess = (max + min) // 2

while current_guess != random_number:
    if random_number < current_guess:
        max = current_guess - 1
    else:
        min = current_guess + 1
    
    current_guess = (max + min) // 2


print("Guess: ", current_guess)
print("True: ", random_number)