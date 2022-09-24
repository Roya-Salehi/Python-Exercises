is_guess_wrong = True
the_word = [*"EVAPORATE".upper()]
plyr_guess = []
words_len = len(the_word)
progress = [*("_" * words_len)]
print(' '.join(progress) + '\n')

while is_guess_wrong:

    index_list = [0]
    input_guess = input("Guess a letter: ")[0].upper()

    if input_guess in plyr_guess:
        print("You have guessed this letter before.")

    else:
        plyr_guess.append(input_guess)
        count = the_word.count(plyr_guess[-1])
        
        for i in range(count):
            index_list.append(the_word.index(plyr_guess[-1], index_list[i]) + 1)
        index_list.pop(0)

        if index_list:
            for indx in index_list:
                indx = indx - 1
                progress.pop(indx)
                progress.insert(indx, plyr_guess[-1])
                
            if "_" not in progress:
                is_guess_wrong = False
                print('\n' + ''.join(progress) + '\n')
                print(f"Congratulations! You guessed the word in {len(plyr_guess)} moves.")
            else:
                print('\n' + ' '.join(progress) + '\n')
        else:
            print("Incorrect!")
    
