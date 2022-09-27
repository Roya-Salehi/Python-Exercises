import json
import math
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open("./assets/birthdaysdictionary.json", 'r') as file:
    birthdays_dict = json.load(file)
list_of_all_months = ["January", "February", "March", "April", "May",
                      "June", "July", "August", "September", "October", "November", "December"]
bd_months = []
for birthday in birthdays_dict.values():
    bd_months.append(birthday.split()[0])
count_months = Counter(bd_months)

output_file("./assets/plot.html")
p = figure(x_range=list_of_all_months, title="Scientists' Birthday Months")
p.xaxis.major_label_orientation = math.pi/4
p.vbar(x=[j for j in count_months.keys()], top=[int(i)
       for i in count_months.values()], width=0.5)
show(p)
