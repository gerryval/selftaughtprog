import random

word_list = ['gato','perro','house','car']

def hangman(word):
    wrong = 0
    stages = ['',
              '_________     ',
              '|             ',
              '|        |    ',
              '|        0    ',
              '|       /|\   ',
              '|       / \   ',
              '|             '
              ]
    remaining_letters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Guess a letter '
        char = input(msg)
        if char in remaining_letters:
            cindex = remaining_letters.index(char)
            board[cindex] = char
            remaining_letters[cindex] = '$'
        else:
            wrong += 1
        print(''.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}.'.format(word))

w = random.choice(word_list)
hangman(w)
