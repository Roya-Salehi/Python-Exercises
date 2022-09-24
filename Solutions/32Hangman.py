import random


def pick_word():
    with open('./assets/sowpods.txt', 'r') as file:
        words_list = file.read().splitlines()
        random_word = random.choice(words_list)

    return random_word


def build_hangman(wrong_moves):
    head, rhand, lhand, body, rleg, lleg = '', ' ', ' ', ' ', ' ', ' '

    if wrong_moves == 0:
        head, rhand, lhand, body, rleg, lleg = '(_)', '\\', '/', '|', '\\', '/'
    elif wrong_moves == 1:
        head, rhand, lhand, body, rleg = '(_)', '\\', '/', '|', '\\'
    elif wrong_moves == 2:
        head, rhand, lhand, body = '(_)', '\\', '/', '|'
    elif wrong_moves == 3:
        head, rhand, lhand = '(_)', '\\', '/'
    elif wrong_moves == 4:
        head, rhand = '(_)', '\\'
    elif wrong_moves == 5:
        head = '(_)'

    print(" " * 5 + "_" * 7 + " ")
    print(" " * 4 + "|" + "/" + " " * 6 + "|")
    print(" " * 4 + "|" + " " * 7 + "|")
    print(" " * 4 + "|" + " " * 6 + head)
    print(" " * 4 + "|" + " " * 6 + lhand + body + rhand)
    print(" " * 4 + "|" + " " * 7 + body)
    print(" " * 4 + "|" + " " * 6 + lleg + " " + rleg)
    print(" " * 4 + "|")
    print("_" * 4 + "|" + "_" * 4 + "\n")


def new_game():
    answer = input("Do you want to play again? [y/n]: ")[0].lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False


is_new_game = True

while is_new_game:
    the_word = [*pick_word().upper()]
    is_guess_wrong = True
    plyr_guess = []
    incorrect_guess = 0
    words_len = len(the_word)
    progress = [*("_" * words_len)]
    print(' '.join(progress) + '\n')

    while is_guess_wrong:
        if incorrect_guess == 6:
            print("You lost the game.")
            print(f"The word was {''.join(the_word)}.")
            is_new_game = new_game()
            break

        index_list = [0]
        input_guess = input("Guess a letter: ")[0].upper()

        if input_guess in plyr_guess:
            print("You have guessed this letter before.")

        else:
            plyr_guess.append(input_guess)
            count = the_word.count(plyr_guess[-1])

            for i in range(count):
                index_list.append(the_word.index(
                    plyr_guess[-1], index_list[i]) + 1)
            index_list.pop(0)

            if index_list:
                for indx in index_list:
                    indx = indx - 1
                    progress.pop(indx)
                    progress.insert(indx, plyr_guess[-1])

                if "_" not in progress:
                    is_guess_wrong = False
                    print('\n' + ''.join(progress) + '\n')
                    print(
                        f"Congratulations! You guessed the word in {len(plyr_guess)} moves.")
                    is_new_game = new_game()
                    break

                else:
                    print('\n' + ' '.join(progress) + '\n')
            else:
                incorrect_guess += 1
                print(f"Incorrect!")

            build_hangman(incorrect_guess)
