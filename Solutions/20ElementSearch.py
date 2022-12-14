def simple_list_search(olist, number):
    olist.sort()
    for n in olist:
        if n == number:
            return True
    return False


def binary_list_search(olist, number):
    olist.sort()
    lenght = len(olist)
    while True:
        mindex = len(olist) // 2
        if olist[mindex] == number:
            return True
        elif mindex == 0:
            return False
        elif olist[mindex] > number:
            olist = olist[:mindex]
        elif olist[mindex] < number:
            olist = olist[mindex + 1:]


olist = list(map(int, input("Enter a list of numbers: ").strip().split()))
number = int(input("Enter the number to search for: "))
print(simple_list_search(olist, number))
print(binary_list_search(olist, number))
