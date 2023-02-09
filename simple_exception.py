name = input("What is your name? ")
age = input("How old will you be this year? ")
try:
    age = int(age)
    birth_year = 2023 - age
except ValueError:
    print("sorry, that was not a valid number")
    exit(1)
except NameError:
    print("oh, it's not you, it's me :)")
    exit(1)
else:
    print(name, "you were born in", birth_year)
finally:
    print("Thanks for playing, come again")