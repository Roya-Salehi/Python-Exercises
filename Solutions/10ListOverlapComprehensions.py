import random
import random

# ******    Solution by using sets:   ******
# result = set(random.randrange(50) for i in range(random.randint(0, 20))).intersection(
#     set(random.randrange(50) for i in range(random.randint(0, 20))))
# print(list(result))

a = random.choices(range(1, 30), k=12)
b = random.choices(range(1, 30), k=16)
result = list(dict.fromkeys(n for n in a if n in b))
a.sort()
b.sort()
result.sort()
print(f"a = {a}\nb = {b}\nresult = {result}")
