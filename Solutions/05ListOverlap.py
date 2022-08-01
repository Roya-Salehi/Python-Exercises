import random
a = [random.randrange(50) for i in range(random.randint(0, 20))]
b = [random.randrange(50) for i in range(random.randint(0, 20))]
a.sort()
b.sort()
print(f"a = {a}\nb = {b}\n")
print(list(dict.fromkeys(n for n in a if n in b)))
print(list(set([n for n in a if n in b])))
