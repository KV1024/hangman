#!/usr/bin/env python3

def hangman(word):
    wrong = 0
    stages = ["",
            "____________  ",
            "|          |  ",
            "|          O  ",
            "|         /|\ ",
            "|         / \ ",
            "|             "
            ]
    rletters = list(word)   # creates a list of all characters in word ['p', 'o', 't', 'a', 't', 'o']
    board = ["_ "] * len(word)
    win = False
    print("Hello, it's time to be publicly executed for incorrectly guessing some letters! :D")
    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter: ")
        if char in rletters:
            char_idx = rletters.index(char)
            board[char_idx] = char  # puts the character in place of underscore at right index in board
            rletters[char_idx] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        x = wrong + 1
        print("\n".join(stages[0: x]))
        if "_ " not in board:
            print("You win. \n Be happy.")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You just got publicly executed for incorrectly guessing some letters, loser. \nIt was {}.".format(word))

hangman("potato")