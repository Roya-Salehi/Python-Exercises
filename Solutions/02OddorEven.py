num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
OddorEven = "odd" if num % 2 else "even"
print(f"The number {num} is a multiple of 4.") if num % 4 == 0 else print(
    f"The number {num} is {OddorEven}.")
print(f"{check} is not a factor of {num}.") if num % check else print(
    f"{check} is a factor of {num}.")
