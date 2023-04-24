import random
import math

min = -29389518293123
max = 92301239132060
random_number = random.randint(min, max)

iterations = int(math.log(1 / (max-min), 0.5)) + 1
for i in range(iterations):
    midpoint = (max + min) // 2
    if random_number < midpoint:
        max = midpoint
    else:
        min = midpoint

guess = min if min == random_number else max