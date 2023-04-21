import random
import math

min = -2392983243015912
max = 1923922392349823

random_number = random.randint(min, max)

while min != max:
    midpoint = (max + min) / 2
    if random_number < midpoint:
        max = math.floor(midpoint)
    else:
        min = math.ceil(midpoint)

print("Guess: ", min)
print("True: ", random_number)