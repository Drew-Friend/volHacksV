import json

name = ""
over = False
playerList = ["NA"]


def readF():
    # try:
    with open("games/log.txt") as json_file:
        data = json.load(json_file)
    return data


def writeF(new):
    try:
        with open("games/log.txt", "w") as json_file:
            json.dump(new, json_file)
    except:
        writeF(new)


def getName():
    return input("Give us a name to add to you message: ")


def turn(file, room, player):
    global name, over
    if name == "":
        name = getName()
    data = readF()
    printSquare()
    mess = input("Input your message, or 'quit' to exit")
    if mess == "quit":
        over = True
        return "1_"
    newline = {"Name": name, "message": mess}
    data["Chat"] = data["Chat"][1:]
    data["Chat"].append(newline)
    writeF(data)
    return "1_"


def showBoard():
    print(
        "Here's a chat room for chilling with other UT students! Just type 'quit' to exit!"
    )


def printSquare(trash=""):
    data = readF()
    for i in data["Chat"]:
        print(i["Name"], end=":  ")
        print(i["message"])
    print()


def winCheck(trash, garbage):
    return over
