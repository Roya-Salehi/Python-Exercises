import random
a = [random.randrange(50) for _ in range(random.randint(0, 20))]
b = [random.randrange(50) for _ in range(random.randint(0, 20))]
print(f"a = {sorted(a)}\nb = {sorted(b)}\n")
print(sorted(list(dict.fromkeys(n for n in a if n in b))))
print(sorted(list(set([n for n in a if n in b]))))
