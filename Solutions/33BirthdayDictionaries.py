def lookup(birthdays_dict):
    name = input("Whose birthday do you want to know? ").lower()
    for key, value in birthdays_dict.items():
        if key.lower().startswith(name):
            print(f"{key} was born on {value}.")
            return 0
    return name


birthdays_dict = {'Albert Einstein': 'March 14, 1879',
                  'Benjamin Franklin': 'January 17, 1706', 'Ada Lovelace': 'December 10, 1815'}

print("Welcome to the birthday dictionary. We know the birthdays of:\n" +
      "\n".join(birthdays_dict.keys()))

result = lookup(birthdays_dict)
if result: print(f"We don't have the birthday of {result}.")

