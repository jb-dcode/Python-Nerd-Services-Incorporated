import random
random_number = random.randint(0, 100)

x = range(0, 100, random_number)
for n in x:
  print(n)
  print(x[1:2])
