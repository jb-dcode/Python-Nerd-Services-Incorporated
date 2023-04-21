"""In this exercise, I had create the solution for the challenge, however, I just have the code offuscated
by removing the name of the variables, so you will need to put a proper name for the variables and function and
comment what each portion is doing after the # symbol.

May the odds be on your favor.

-Jesus
"""


import random

# generates a uniformly distributed random integer between those numbers
random_number = random.randint(-29389518293123, 92301239132060)


# uses the midpoint between low and high to exclude half of the remaining possible values in the range per iteration. calls itself until current_guess == random_number
def s(low, high, random_number, iterations):
    # googled this because I've never seen // before (kinda cheating, sorry), but basically equivalent to floor((l + h) / 2)
    # calculates one of the integer midpoints and increments counter for # of iterations
    current_guess = (low + high) // 2
    iterations += 1

    # stops recursion when we've found the correct number, and returns the found value and total number of iterations
    if current_guess == random_number:
        return current_guess, iterations

    # the random number is less than our current guess, so all values >= can be excluded. iterate again with new upper bound.
    elif current_guess > random_number:
        return s(low, current_guess - 1, random_number, iterations)

    # the random number is greater than our curren guess, so all values <= can be excluded. iterate again with new lower bound.
    else:
        return s(current_guess + 1, high, random_number, iterations)


# recursively identifies the random number and counts the number of iterations it took, then sets those values equal to "guess" and "iterations"
guess, iterations = s(-29389518293123, 92301239132060, random_number, 0)

# prints the random number and iteration variables
print("asdfasdfasdf:", random_number)
print("asdfasdfasdf:", iterations)