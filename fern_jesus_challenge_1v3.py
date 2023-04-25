import random

min = -29389518293123
max = 92301239132060
random_number = random.randint(min, max)

iterations = int.bit_length(max-min)
for i in range(iterations):
    midpoint = (max + min) // 2
    if random_number < midpoint:
        max = midpoint
    else:
        min = midpoint

guess = min if min == random_number else max