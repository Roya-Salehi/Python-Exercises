prime_numbers_set = []
happy_numbers_set = []

with open('./assets/primenumbers.txt', 'r') as prime_numbers_file:
    prime_numbers_set = set(prime_numbers_file.read().split())

with open('./assets/happynumbers.txt', 'r') as happy_numbers_file:
    happy_numbers_set = set(happy_numbers_file.read().split())

print(list(prime_numbers_set.intersection(happy_numbers_set)))
