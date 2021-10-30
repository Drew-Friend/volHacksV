# 1 2 3
# 4 5 6
# 7 8 9
playerList = ["X", "O"]


def turn(file, room, player):
    squareStr = file[room]["state"]
    squares = []
    for i in squareStr:
        squares.append(i)
    playerSign = "O"
    if player == 1:
        playerSign = "X"
    printSquare(squares)
    try:
        pX = int(input("Please select a square:  "))
    except:
        pX = int(input("Please select a square:  "))
    choosing = True
    while choosing:
        if moveCheck(pX, squares):
            squares[pX] = playerSign
            choosing = False
        else:
            try:
                pX = int(input("Please select a square:  "))
            except:
                pX = int(input("Please select a square:  "))
            continue
    printSquare(squares)

    squareStr = ""
    if squares[0] == "1":
        squares[0] = "2"
    else:
        squares[0] = "1"
    for i in squares:
        squareStr += i
    return squareStr


def printSquare(squares):  # display the board
    # row 1
    print(squares[1], end=" "),
    print(squares[2], end=" "),
    print(squares[3]),
    # row 2
    print(squares[4], end=" "),
    print(squares[5], end=" "),
    print(squares[6]),
    # row 3
    print(squares[7], end=" "),
    print(squares[8], end=" "),
    print(squares[9])
    print("")


def moveCheck(choice, squares):  # check validity of move
    if choice > 0 and choice < 10 and squares[choice] == "_":
        return True
    else:
        return False


def winCheck(player, squares):  # check if someone won
    if squares[5] == player:
        if squares[1] == player and squares[9] == player:  # \ diagonal
            print("Player {} wins!!".format(player))
            return True
        elif squares[3] == player and squares[7] == player:  # / diagonal
            print("Player {} wins!!".format(player))
            return True
        elif squares[2] == player and squares[8] == player:  # middle column
            print("Player {} wins!!".format(player))
            return True
        elif squares[4] == player and squares[6] == player:  # middle row
            print("Player {} wins!!".format(player))
            return True
    if squares[7] == player:
        if squares[1] == player and squares[4] == player:  # first column
            print("Player {} wins!!".format(player))
            return True
        elif squares[8] == player and squares[9] == player:  # bottom row
            print("Player {} wins!!".format(player))
            return True
    if squares[3] == player:
        if squares[6] == player and squares[9] == player:  # final column
            print("Player {} wins!!".format(player))
            return True
        elif squares[1] == player and squares[2] == player:  # top row
            print("Player {} wins!!".format(player))
            return True
    else:
        return False


def showBoard():
    print(" 1 2 3\n 4 5 6\n 7 8 9")
