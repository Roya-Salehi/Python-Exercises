from ctypes import pointer
import imp


import random
print("******      Try to guess the number from 1 to 9. To end the game, enter 'exit'.     ******")
while True:
    num = random.randint(1, 9)
    user = input("Enter your guess, from 1 to 9: ")
    track = 1
    if user.lower() == 'exit':
        break
    while user.lower() != 'exit':
        user = int(user)
        if user == num:
            print("Congratulations! You guessed exactly right.")
            print(f"You took {track} guesses.")
            print("***  Next Round  ***")
            break
        elif user < num:
            print("You guessed too low. Try again.")
        elif user > num:
            print("You guessed too high. Try again.")
        user = input("Guess again: ")
        track += 1
