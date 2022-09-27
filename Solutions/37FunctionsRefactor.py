def create_board(x, y):
    lines = y * 2 + 1
    for l in range(lines):
        for i in range(x):
            if l % 2:
                print("|   ", end='')
            else:
                print(" ---", end='')
        if l % 2:
            print("|", end='')
        print()


rows, columns = input(
    "Enter how many rows ans columns should the board have? [rows, columns]: ").split(",")
create_board(int(rows), int(columns))
