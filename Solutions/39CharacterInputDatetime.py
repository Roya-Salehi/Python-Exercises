from datetime import datetime

current_year = datetime.now().year
name = input("Your name: ")
age = int(input("Your age: "))
print(f"{name} will be 100 years old in {current_year - age + 100}.")