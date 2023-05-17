from datetime import datetime

def salute(name, birth_year, gender, favorite_number):
    # Get pronoun from gender
    pronoun = "Sirmissus Spectacularanasourus"
    if gender == "Male" or gender == "Man":
        pronoun = "Dude"
    elif gender == "Female" or gender == "Woman":
        pronoun = "Lass"

    # Get age from birth year
    current_date = datetime.today()
    age = current_date.year - birth_year
    if current_date.month < 7:
        age -= 1

    # Print salutation
    print("Hello " + pronoun + "!")
    print("I understand that you, " + name + ", are (probably) " + str(age) + " years old. That's awesome!")
    print("You've also told us that your favorite number is " + str(favorite_number) + "!")

    # Do some loop with favorite number
    min = 1 if favorite_number > 0 else -1
    multiplied = 1
    for n in range(min, favorite_number, min):
        multiplied *= n
    
    if favorite_number == 0:
        min = 0
        multiplied = 0

    multiplied = "{:,}".format(multiplied)

    print("\nDid you know?")
    print("If you multiply all the numbers from " + str(min) + " to " + str(favorite_number) + " you get " + str(multiplied) + "?")


salute("Cleopatra", -69, "Pharaohess", 7)