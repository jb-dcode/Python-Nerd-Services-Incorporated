x = 5
y = 10

# If statement
# This is a simple if statement, only do operations when something is true
if x < y:
    print("x is less than y")

# If-else statement
# This conditional works when having a true and a false operation
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# If-elif-else statement
# This one is interesting as you have three different options and depending on which one it falls
# it will do the actions.
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Nested if statement
# This one we do nested IF statements, inside an IF you open another IF, and Python will detect the
# different IFs due the indentation.
if x < y:
    if x < 0:
        print("x is negative and less than y")
    else:
        print("x is positive and less than y")

# Ternary operator
# The Ternary operator is using a conditional within the assigntment of a variable, here it is just a example.
result = "x is less than y" if x < y else "x is not less than y"
print(result)