import timeit


setup = "import random; import math; random.seed(0)"

v1 = """
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
"""

v3_old = """
min = -29389518293123
max = 92301239132060
random_number = random.randint(min, max)

while min != max:
  midpoint = (max + min) / 2
  if random_number < midpoint:
    max = math.floor(midpoint)
  else:
    min = math.ceil(midpoint)
"""

jv = """
random_number = random.randint(-29389518293123, 92301239132060)

def s(low, high, random_number):
  current_guess = (low + high) // 2

  if current_guess == random_number:
    return current_guess
  elif current_guess > random_number:
    return s(low, current_guess - 1, random_number)
  else:
    return s(current_guess + 1, high, random_number)

s(-29389518293123, 92301239132060, random_number)
"""

v3_new = """
min = -29389518293123
max = 92301239132060
random_number = random.randint(min, max)

iterations = int.bit_length(max-min)
for i in range(0, iterations):
    midpoint = (max + min) // 2
    if random_number < midpoint:
        max = midpoint
    else:
        min = midpoint

guess = min if min == random_number else max
"""

print(timeit.timeit(v1, setup, number=1000000))
#print(timeit.timeit(v3_old, setup, number=1000000))
print(timeit.timeit(jv, setup, number=1000000))
print(timeit.timeit(v3_new, setup, number=1000000))