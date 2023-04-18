import random

min = -999
max = 999

random_number = random.randint(min, max)

current_guess = round((max + min) / 2)

while current_guess != random_number:
    if random_number < current_guess:
        max = current_guess - 1
    else:
        min = current_guess + 1
    
    current_guess = round((max + min) / 2) 


print("Guess: ", current_guess)
print("True: ", random_number)