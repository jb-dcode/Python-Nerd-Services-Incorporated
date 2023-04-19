import random

# "rn" is a random number that can be anywhere between those two parameters. i have changed this to "num_rand"
num_rand = random.randint(-29389518293123, 92301239132060)


# "def" is defining a function. "s" is the name of the function originally, but i am now calling this function "select".
least = -29389518293123
highest = 92301239132060


def select(least, highest, num_rand, i):

    # "cg" is now "current_guess" aka l+h, and then dividing that answer by 2. this will get the average to compare.
    # i += 1 is equivalent to the expression: i = i + 1. i can remain as it is; it usually would stand for integer
    current_guess = (least + highest) // 2
    i += 1

    # a conditional. if is supposed to act as my "for" loop in this situation, except it's just not looping.
    if current_guess == num_rand:
        return current_guess, i

    # if they are not equal to each other, python will check this next.
    elif current_guess > num_rand:
        return select(least, current_guess - 1, num_rand, i)

    # if both if and elif are not satisfied, then the computer will go for this option automatically.
    else:
        return select(current_guess + 1, highest, num_rand, i)


# we are now revising our guess AND the average to include these parameters.
current_guess, i = select(-29389518293123, 92301239132060, num_rand, 0)

# we are now printing to compare the random number, to the guess the algorithm made.
print("secret number:", num_rand)
print("algorithm's guess:", i)