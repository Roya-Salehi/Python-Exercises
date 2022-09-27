from calendar import month
import json
from collections import Counter

with open("./assets/birthdaysdictionary.json", 'r') as file:
    birthdays_dict = json.load(file)

months = []
for birthday in birthdays_dict.values():
    months.append(birthday.split()[0])

count_months = Counter(months)
print(count_months)