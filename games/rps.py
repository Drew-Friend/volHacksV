# 1 2 3
# 4 5 6
# 7 8 9
playerList = ["1", "2"]
choiceList = ["r", "p", "s"]


def turn(file, room, player):
    gameState = file[room]["state"]
    print("Rock..")
    print("Paper..")
    print("Scissors..")
    choice = input("Shoot! ")
    while True:
        for i in choiceList:
            if choice == i:
                gameState = gameState[:player] + i + gameState[player + 1 :]
                return gameState
        choice = input("Input Valid Code")


def printSquare(squares):  # display the board
    print("", end="")


def winCheck(player, file):  # check if someone won
    gameState = file
    c1 = file[1]
    c2 = file[2]
    if c1 == c2:
        if c1 != "_":
            print("It's a tie! Go again!")
        return False
    if c1 == "r":
        if c2 == "s":
            print("Player 1 Wins!")
            return True
        if c2 == "p":
            print("Player 2 Wins")
            return True
    if c1 == "p":
        if c2 == "r":
            print("Player 1 Wins!")
            return True
        if c2 == "s":
            print("Player 2 Wins")
            return True
    if c1 == "s":
        if c2 == "p":
            print("Player 1 Wins!")
            return True
        if c2 == "r":
            print("Player 2 Wins")
            return True


def showBoard():
    print("Type 'r' for Rock, 'p' for Paper, and 's' for Scissors")
