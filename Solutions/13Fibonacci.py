def fibonacci(num):
    seq = [1, 1]
    for i in range(2, num):
        seq.append(seq[i-1]+seq[i-2])
    return seq[:num]


num = int(input("Enter a number: "))
print(fibonacci(num))
