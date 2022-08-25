from ast import Break
from random import sample, shuffle


'''
*** Bulls and Cows Game Rules:
The player guesses a 4-digit number. The digits of the number guessed must all be different.
If the matching digits are in their right positions, they are "bulls", if in different positions, they are "cows".
'''


def check_guess(guess, number):
    guesslist = list(map(int, str(guess)))
    numlist = list(map(int, str(number)))
    bulls, cows = 0, 0
    for i in range(len(guesslist)):
        if guesslist[i] == numlist[i]:
            bulls += 1
        elif guesslist[i] in numlist:
            cows += 1
    return bulls, cows


# *** Generate a 4-digit number with no repeating digits
numbers = sample(range(10), 4)
while numbers[0] == 0:
    shuffle(numbers)
num = int(''.join(map(str, numbers)))
guess = 0
print("Enter exit to terminate the game.")

while guess != num:
    guess = input("Enter a 4-digit number: ")
    if guess.lower() == 'exit':
        print(f"The original number was {num}.")
        break
    try:
        guess = int(guess)
        if guess > 9999 or guess < 1000:
            raise ValueError("Invalid Number: %s" % guess)
    except ValueError:
        raise ValueError("Invalid Input: %s" % guess)
    else:
        bulls, cows = check_guess(guess, num)
        bullexp, cowexp = "bulls", "cows"
        if bulls == 1:
            bullexp = "bull"
        if cows == 1:
            cowexp = "cow"
        print(f"{bulls} {bullexp}, {cows} {cowexp}")
    

if guess == num:
    print("Congratulations! You won.")
