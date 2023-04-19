import random

random_number = random.randint(-29389518293123, 92301239132060)


current_guess = 0
increment = 1

while current_guess != random_number:
    if increment > 0 and random_number < current_guess:
        increment = -1
    elif increment < 0 and random_number > current_guess:
        increment = 1
    
    else:
        current_guess += increment
        increment *= 2
    

print("Guess: ", current_guess)
print("True: ", random_number)