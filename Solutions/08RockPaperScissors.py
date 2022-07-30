print("*****        Enter 'r' for 'rock', 'p' for 'paper', 's' for 'scissors'.      *****")
while True:
    fplr = input("First player: ").lower()
    splr = input("Second player: ").lower()

    if fplr == splr:
        print("It's a tie!")
    elif fplr == 'r':
        print("The second palyer won!") if splr == 'p' else print(
            "The first palyer won!")
    elif fplr == 'p':
        print("The second palyer won!") if splr == 's' else print(
            "The first palyer won!")
    elif fplr == 's':
        print("The second palyer won!") if splr == 'r' else print(
            "The first palyer won!")
    else:
        print("Invalid input! Please try again.")
    cont = input("Do you want to play again? ").lower()
    if cont[0] == 'n':
        break
