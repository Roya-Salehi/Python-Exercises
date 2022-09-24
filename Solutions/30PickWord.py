import random


def pick_word():
    with open('./assets/sowpods.txt', 'r') as file:
        words_list = file.read().splitlines()
        random_word = random.choice(words_list.strip())

    return random_word


print(pick_word())
