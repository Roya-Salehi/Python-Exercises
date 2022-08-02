def reverse_order(sent):
    lst = list(sent.split(" "))
    blst = lst[::-1]
    return " ".join(blst)


sent = input("Enter a sentence: ")
print(reverse_order(sent))

# ******      Single line code:     ******
# print(" ".join(input("Enter a sentence: ").split()[::-1]))
