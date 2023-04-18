import random

random_number = random.randint(0, 100)

min = 0
max = 100

current_guess = round((max + min) / 2)

while current_guess != random_number:
    if random_number < current_guess:
        max = current_guess
    else:
        min = current_guess
    
    current_guess = round((max + min) / 2)



print("Guess: ", current_guess)
print("True: ", random_number)