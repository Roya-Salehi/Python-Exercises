def get_move(player):
    if player == "x":
        player_one = input("X: ").split(",")
        return [int(i) for i in player_one]
    else:
        player_two = input("O: ").split(",")
        return [int(i) for i in player_two]


def play_move(player, move, game, filler):
    for i in move:
        if i > 3 or i <= 0:
            print("Error: Out of range!")
            return 0

    if len(move) != 2:
        print("Error: Invalid move!")
        return 0

    elif game[move[0] - 1][move[1] - 1] == filler:
        game[move[0] - 1][move[1] - 1] = player
        return game

    elif game[move[0] - 1][move[1] - 1] != filler:
        print("Error: The move has already been played.")
        return 0


filler = ' '
game = [[filler]*3 for _ in range(3)]

print(
    "Enter your moves in such format: row, column [Valid inputs fr row and column; 1, 2 or 3]")

j = 0
while True:
    played = 0
    for row in game:
        print(row)
        for i in row:
            if i != filler:
                played += 1

    if played == 9:
        break

    elif j % 2:
        while True:
            o_location = get_move("o")
            play_result = play_move("o", o_location, game, filler)
            if play_result:
                game = play_result
                j += 1
                break

    elif j % 2 == 0:
        while True:
            x_location = get_move("x")
            play_result = play_move("x", x_location, game, filler)
            if play_result:
                game = play_result
                j += 1
                break
