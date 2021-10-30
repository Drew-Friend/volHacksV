# 1 2 3
# 4 5 6
# 7 8 9
playerList = ["1"]
choiceList = ["r", "p", "s"]
import json


def turn(file, room, player):
    gameState = file[room]["state"]
    if gameState[0] == "1":
        gameState = "2" + gameState[1:]
    else:
        gameState = "2" + gameState[1:]
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
    strTot = "2" + c1 + c2
    if c1 == c2:
        if c1 != "_":
            print("It's a tie! Go again!")
            with open("./data.txt") as json_file:
                data = json.load(json_file)
            for i in data["Rock Paper Scissors"]:
                if i["state"] == strTot:
                    i["state"] = "1__"
            with open("./data.txt", "w") as json_file:
                json.dump(data, json_file)

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
