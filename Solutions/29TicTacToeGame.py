def build_board(char=' '):
    size = 3

    def update_board(grow_indx, gscore_indx, player):
        if grow_indx == 0:
            brow_indx = 1
        elif grow_indx == 1:
            brow_indx = 3
        elif grow_indx == 2:
            brow_indx = 5
        if gscore_indx == 0:
            bscore_indx = 2
        elif gscore_indx == 1:
            bscore_indx = 6
        elif gscore_indx == 2:
            bscore_indx = 10
        board[brow_indx][bscore_indx] = player

    # For building the empty game board
    if board == [] and game == []:
        for i in range(size):
            game.append([])
            for _ in range(size):
                game[i].append(0)

        for i in range(size * 2 + 1):
            board.append([])
            if i % 2 == 0:
                for j in range(size * 4 + 1):
                    if j % 4 == 0:
                        board[i].append(' ')
                    else:
                        board[i].append('-')
            else:
                for j in range(size * 4 + 1):
                    if j % 4 == 0:
                        board[i].append('|')
                    elif j % 2 == 0:
                        board[i].append(char)  # filler
                    else:
                        board[i].append(' ')

    # Updating the board
    elif game:
        grow_indx = 0
        for grow in game:
            gscore_indx = 0
            for gscore in grow:
                if gscore == 1:
                    update_board(grow_indx, gscore_indx, 'X')
                elif gscore == 2:
                    update_board(grow_indx, gscore_indx, 'O')
                gscore_indx += 1
            grow_indx += 1


def get_move(player_name, sign):
    move_input = input(f"{player_name} ({sign.upper()}): ").split(",")
    return [int(i) for i in move_input]


def play_move(player, move):
    size = len(game)
    for i in move:
        if i > size or i < 1:
            print("Error: Out of range!")
            return 0

    if len(move) != 2:
        print("Error: Invalid move!")
        return 0

    elif game[move[0] - 1][move[1] - 1] != 0:
        print("Error: The move has already been played.")
        return 0

    elif game[move[0] - 1][move[1] - 1] == 0:
        game[move[0] - 1][move[1] - 1] = player
        build_board()
        return 1

    else:
        print("Somthing went wrong!")
        return 0


def play(player_name, player_number, sign, j):
    while True:
        move = get_move(player_name, sign)
        play_result = play_move(player_number, move)
        if play_result:
            j += 1
            break
    return j


def check_game():
    size = len(game)
    diagonal_nums_l2r = []
    diagonal_nums_r2l = []
    i = size - 1

    for indx in range(size):
        # Check the rows to see if any of the players has won;
        for num in game[indx]:
            if game[indx].count(num) == size and num != 0:
                return num

        # Check the columns and the diagonals to see if any of the players has won;
        column_nums = []
        for row in range(size):
            column_nums.append(game[row][indx])
            if indx == row:
                diagonal_nums_l2r.append(game[indx][indx])

        if i >= 0:
            diagonal_nums_r2l.append(game[indx][i])
            i -= 1

        if len(set(column_nums)) == 1 and column_nums[0] != 0:
            return column_nums[0]

    if len(set(diagonal_nums_l2r)) == 1 and diagonal_nums_l2r[0] != 0:
        return diagonal_nums_l2r[0]
    elif len(set(diagonal_nums_r2l)) == 1 and diagonal_nums_r2l[0] != 0:
        return diagonal_nums_r2l[0]
    else:
        return 0


# Start new game settings
players_scores = [0, 0]
gset = 1
keep_playing = True
player_name_1 = input("Player one, enter your name: ")
player_name_2 = input("Player two, enter your name: ")

while keep_playing:
    filler = ' '
    board = []
    game = []

    #  Build the empty board game
    build_board(filler)

    # The guide for the game
    print(f"\n=============== Round {gset} =================")
    print(
        "Enter your moves in such format: row, column [Valid inputs for row and column; 1, 2 or 3]")

    j = 0
    winner = False

    while True:
        # Print the board game
        for line in board:
            for item in line:
                print(item, end='')
            print()

        # Check if any player has won
        final_result = check_game()
        if final_result != 0:
            winner = True
            players_scores[final_result - 1] += 1
            break

        # Check if there is any move left
        played = 0
        for row in game:
            for i in row:
                if i != 0:
                    played += 1
        if played == 9:
            break

        # Second Player's turn to make a move
        elif j % 2:
            j = play(player_name_2, 2, "o", j)

        # First Player's turn to make a move
        elif j % 2 == 0:
            j = play(player_name_1, 1, "x", j)

    # Print the game set result
    if winner:
        if final_result == 1:
            print(f"Congratulations! {player_name_1} has won this round.")
        elif final_result == 2:
            print(f"Congratulations! {player_name_2} has won this round.")
    else:
        print("Tie! No winner.")

    print(
        f"Scores: {player_name_1} = {players_scores[0]} | {player_name_2} = {players_scores[1]}")

    # Check if the players want to continue playing
    answer = input("Do you want to continue (y / n)? ").lower()[0]
    keep_playing = True if answer == "y" else False
    gset += 1

    # Switch players
    player_name_1, player_name_2 = player_name_2, player_name_1
    players_scores.reverse()
