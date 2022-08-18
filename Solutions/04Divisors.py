number = int(input("Enter a number: "))
divisors = [number]
for n in range(1, number):
    if number % n == 0:
        divisors.append(n)
print(sorted(divisors))
