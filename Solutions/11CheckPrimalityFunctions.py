def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return "is not"
    return "is"


number = int(input("Enter a number: "))
result = check_prime(number)
print(f"{number} {result} a prime number.")
