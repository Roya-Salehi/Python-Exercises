import random


def list_ends(lenght, start, end):
    try:
        lenght = int(lenght)
        start = int(start)
        end = int(end)
        org_list = random.sample(range(start, end), lenght)
        new_list = [org_list[0], org_list[-1]]
    except:
        if start > end:
            print("The start number cannot be bigger than the end.")
        elif lenght <= 0:
            print("The lenght of the list cannot be zero or negative.")
        else:
            print("invalid input.")
        return None, None
    else:
        return org_list, new_list


lenght = input("Enter the lenght of the list: ")
start = input("Enter the start of the range: ")
end = input("Enter the end of the range: ")
a, b = list_ends(lenght, start, end)
if a != None:
    print(f"list = {a}\nnew list = {b}")
