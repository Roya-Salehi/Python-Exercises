import random


def check_guess():
    cp = random.randint(1, 9)
    point = 0
    while True:
        guess = input("Guess a number from 1 to 9: ")
        point += 1
        try:
            guess = int(guess)
        except:
            if guess == "exit":
                return 20
            else:
                print("Invalid input! Try again.")
                # We subtrack 1 point so this guess wouldn't count in the result.
                point -= 1
                continue
        else:
            if guess not in range(1, 10):
                print("Your number is out of the specified range. Try again!")
                # We subtrack 1 point so this guess wouldn't count in the result.
                point -= 1
                continue
            elif guess == cp:
                print("You guessed right. Congratulations!")
                return point
            elif guess < cp:
                print("You guessed too low.")
            else:
                print("You guessed too high.")


result = 0
while True:
    result = check_guess()
    if result == None or result == 20:
        break
    else:
        print(f"You took {result} guesses.\nLet's play again!")
print("Thank you for playing.")
