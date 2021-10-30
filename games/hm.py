import os
import random

# os.system("cls" if os.name == "nt" else "clear")
playerList = ["1"]
# Start all caps, guessed letters become lowercase
wordList = ["FUNNY", "ASKEW", "LUCKY", "VIXEN", "OVARY", "HAIKU"]
numGuess = 0
guesses = []
counter = [
    ["   ___  ", "  / _ \ ", " | | | |", " | | | |", " | |_| |", "  \___/ "],  # 0
    ["  __ ", " /_ |", "  | |", "  | |", "  | |", "  |_|"],  # 1
    [" ___  ", "|__ \\ ", "   ) |", "  / / ", " / /_ ", "|____|"],  # 2
    ["  ____  ", " |___ \ ", "   __) |", "  |__ < ", "  ___) |", " |____/ "],  # 3
    ["  _  _   ", " | || |  ", " | || |_ ", " |__   _|", "    | |  ", "    |_|  "],  # 4
    ["  _____ ", " | ____|", " | |__  ", " |___ \ ", "  ___) |", " |____/ "],  # 5
    ["    __  ", "   / /  ", "  / /_  ", " | '_ \ ", " | (_) |", "  \___/ "],  # 6
    ["  ______ ", " |____  |", "     / / ", "    / /  ", "   / /   ", "  /_/    "],  # 7
    ["   ___  ", "  / _ \ ", " | (_) |", "  > _ < ", " | (_) |", "  \___/ "],  # 8
    ["   ___  ", "  / _ \ ", " | (_) |", "  \__, |", "    / / ", "   /_/  "],  # 9
]


def randomize():
    return random.randint(0, 5)


def turn(file, room, player):
    global numGuess
    done = False
    if numGuess == 0:
        index = randomize()
        # word = file[room]["state"]
        word = "1" + wordList[index]
    else:
        word = file[room]["state"]
    numGuess += 1

    printSquare(word)

    while not done:
        guess = input("Please guess a letter:  ")
        try:
            guess = guess.upper()
            done = True
        except:
            pass

    for i in range(len(word)):
        if word[i] == guess:
            word = word[:i] + guess.lower() + word[i + 1 :]
    guesses.append(guess)
    return word


def printSquare(squares):  # display the board
    os.system("cls" if os.name == "nt" else "clear")

    tens = int(numGuess / 10)
    ones = numGuess % 10
    print(guesses)
    for i in squares[1:]:
        print(" ", end="")
        if i.islower():
            print(i, end="")
        else:
            print("_", end="")
    print("")
    print("Guess Number: ")
    for i in range(6):
        print(counter[tens][i], end="    ")
        print(counter[ones][i])


def moveCheck(choice, squares):  # check validity of move
    pass


def winCheck(player, squares):  # check if someone won
    if squares.islower():
        print("You got it!")
        return True
    return False


def showBoard():
    for i in range(6):
        print(counter[0][i], end="    ")
        print(counter[0][i])
