import json


def print_data():
    print("Birth dates available in the database:\n" +
          "\n".join(birthdays_dict.keys()))
    return 1


def add_data():
    name = input(
        "Whose birthday do you want to add to database? ").capitalize()
    bdate = input(
        f"When is {name}'s birthday? [Month day, year]: ").capitalize()
    birthdays_dict[name] = bdate
    with open("./assets/birthdaysdictionary.json", "w") as file:
        json.dump(birthdays_dict, file)
    return 1


def lookup_data():
    name = input("Whose birthday do you want to know? ").lower()
    for key, value in birthdays_dict.items():
        if name in key.lower():
            print(f"{key} was born on {value}.")
            return 1
    print("Error: Invalid name entered.")
    return 0


with open("./assets/birthdaysdictionary.json", "r") as f:
    birthdays_dict = json.load(f)

while True:
    order = input("What do you want to do? [print, add, find, quit]: ").lower()
    if order.startswith("p"):
        print_data()
    elif order.startswith("a"):
        add_data()
    elif order.startswith("f"):
        lookup_data()
    elif order.startswith("q"):
        print("Good-bye!")
        break
    else:
        print("Error: Invalid Input!")
