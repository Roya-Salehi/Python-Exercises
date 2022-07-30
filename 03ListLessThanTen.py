a = [1, 3, 87, 0, 5, 3, 34, 2, 12]
b = []
for num in a:
    if num < 5:
        b.append(num)
print(b)

# Extra 2
print([num for num in a if num < 5])

# Extra 3
c = int(input("Enter a number: "))
print([num for num in a if num < c])
