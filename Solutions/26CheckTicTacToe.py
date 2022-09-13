def check_game(game):
    players = len(game)
    diagonal_nums_l2r = []
    diagonal_nums_r2l = []
    i = players - 1

    for indx in range(players):
        # Check the rows to see if any of the players has won;
        for num in game[indx]:
            if game[indx].count(num) == players and num != 0:
                return num

        # Check the columns and the diagonals to see if any of the players has won;
        column_nums = []
        for row in range(players):
            column_nums.append(game[row][indx])
            if indx == row:
                diagonal_nums_l2r.append(game[indx][indx])

        if len(set(column_nums)) == 1 and column_nums[0] != 0:
            return column_nums[0]

        if i >= 0:
            diagonal_nums_r2l.append(game[indx][i])
        i -= 1

    if len(set(diagonal_nums_l2r)) == 1 and diagonal_nums_l2r[0] != 0:
        return diagonal_nums_l2r[0]
    elif len(set(diagonal_nums_r2l)) == 1 and diagonal_nums_r2l[0] != 0:
        return diagonal_nums_r2l[0]
    else:
        return 0


winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]

result = check_game(also_no_winner)
print(f"Player {result} is winner.") if result != 0 else print("No winner")
