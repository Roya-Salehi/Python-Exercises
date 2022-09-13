variables_list = input(
    "Enter three variables, seperated by commas: ").split(',')
    
# Check if the inputs are valid
try:
    var1, var2, var3 = [int(number) for number in variables_list]
except:
    raise ValueError("Invalid variables: %s" % variables_list)

if var1 >= var2:
    largest_variable = var1 if var1 >= var3 else var3
else:
    largest_variable = var2 if var2 >= var3 else var3

print(
    f"The largest variable among these numbers ({var1}, {var2}, {var3}) is {largest_variable}.")
