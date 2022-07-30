number = int(input("Enter a number: "))
divisors = []
for n in range(1, number):
    if number % n == 0:
        divisors.append(n)
divisors.sort()
print(divisors)
