def start_game():
    print(
        '''Choose a random number from 1 to 100.
If my guess was lower than your choice, type [l / too low],
if my guess was higher than your choice type [h / too high],
and if my guess was correct type [correct / right].\n''')
    start = input(
        "When you chose your number, enter any key to start the game: ")
    if start:
        return 1


def guess(guess_count):
    possible_guesses = lowest_point + highest_point
    cguess = possible_guesses if possible_guesses == 1 else possible_guesses // 2
    guess_count += 1
    print(f"My guess: {cguess}")
    result = input("Computer's guess is... ")
    yield result
    yield cguess
    yield guess_count


playing = True
guess_count = 0
lowest_point = 1
highest_point = 100

while playing:
    start = start_game()
    if start:
        while True:
            result, cguess, guess_count = guess(guess_count)
            if result.lower() == "correct" or result.lower() == "right":
                print(f"I guessed your number in {guess_count} turns.")
                break
            elif result.lower() == "l" or result.lower() == "too low":
                lowest_point = cguess + 1
            elif result.lower() == "h" or result.lower() == "too high":
                highest_point = cguess - 1
            else:
                print(
                    "Invalid input. Send one of these messages: [l, h, correct]")

    playing = False if input(
        "Do you want to play again? (y / n): ").lower()[0] == "n" else True
