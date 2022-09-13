def board(num):
    for _ in range(0, num * 2, 2):
        print(' ---' * num)
        print('|   ' * num + '|')
    print(' ---' * num)


board(int(input("Board Game Size: ")))
