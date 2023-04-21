"""In this exercise, I had create the solution for the challenge, however, I just have the code offuscated
by removing the name of the variables, so you will need to put a proper name for the variables and function and
comment what each portion is doing after the # symbol.

May the odds be on your favor.

-Jesus
"""


import random

#
rn = random.randint(-29389518293123, 92301239132060)


#
def s(l, h, rn, i):
    #
    cg = (l + h) // 2
    i += 1

    #
    if cg == rn:
        return cg, i

    #
    elif cg > rn:
        return s(l, cg - 1, rn, i)

    #
    else:
        return s(cg + 1, h, rn, i)


#
cg, i = s(-29389518293123, 92301239132060, rn, 0)

#
print("asdfasdfasdf:", rn)
print("asdfasdfasdf:", i)