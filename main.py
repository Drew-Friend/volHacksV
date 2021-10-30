import json
import time
from games import ttt, c4


game = "Selection"
forfeitCount = 0
player = 0
finished = False
ready = False
room = -1
gameDict = {
    "Tic Tac Toe": ttt,
    "Connect 4": c4,
}


class ReadSquares:
    def ttt(data):
        numRooms = 0
        waiting = "     "
        for p in data["Tic Tac Toe"]:
            if p["pop"] != "full":
                numRooms += 1
            if p["pop"] == "waiting":
                waiting = "ready"
        box = [
            " ___________",
            "|  Tic Tac  |",
            "|    Toe    |",
            "|  {} Rooms  |".format(numRooms),
            "|   {}   |".format(waiting),
            "|___________|",
        ]
        for line in range(len(box)):
            print(box[line])


def readF():
    try:
        with open("data.txt") as json_file:
            data = json.load(json_file)
        return data
    except:
        return readF


def writeF(new):
    try:
        with open("data.txt", "w") as json_file:
            json.dump(new, json_file)
    except:
        writeF(new)


def checkTurn(room, player):
    data = readF()
    return (int(data["Tic Tac Toe"][room]["state"][0]) == player), data["Tic Tac Toe"][
        room
    ]["state"]


def checkReady(room):
    data = readF()
    return data["Tic Tac Toe"][room]["pop"] == "full"


def chooseGame(data):
    room = ""
    while True:
        choice = input("Please pick a game listed: ")
        for p in data:
            if p == choice:
                for q in data[choice]:
                    # Find open room if it exists
                    if q["pop"] != "full":
                        room = q["room"]
                        if q["pop"] == "waiting":
                            q["pop"] = "full"
                            return choice, room, 2, data
                        else:
                            q["pop"] = "waiting"
                            return choice, room, 1, data
                if room == "":
                    print("All rooms full, please select another game")


def clearRoom(data):
    data[game][room]["state"] = data[game][0]["state"]
    data[game][room]["pop"] = "empty"
    writeF(data)


# Open The JSON, read it, then close
data = readF()

# Print a UI square of data for each game
# Maybe try to make it 1 iterable method later?
ReadSquares.ttt(data)

# Transition from selection screen to a game
game, room, player, data = chooseGame(data)
room = 1 + int(room)
writeF(data)

print("You are in room {}".format(room))
print("Waiting for match...")
print(
    "If you are in queue 3 minutes, you will be dropped and must re-enter\nThe same is true if you are inactive in a game for 3 minutes"
)
# Wait in queue for 3 minutes or until joined
while not ready and forfeitCount < 1800:
    time.sleep(0.1)
    forfeitCount += 1
    ready = checkReady(room)
if ready:
    forfeitCount = 0
else:
    clearRoom(data)

# Play game until won or forfeited
while not finished and forfeitCount < 1800:
    time.sleep(0.1)
    forfeitCount += 1
    checker, data[game][room]["state"] = checkTurn(room, player)
    for i in gameDict[game].playerList:
        if gameDict[game].winCheck(i, data[game][room]["state"]):
            gameDict[game].printSquare(data[game][room]["state"])
            forfeitCount = 0
            finished = True
    if checker and not finished:
        forfeitCount = 0
        gameDict[game].printSquare(data[game][room]["state"])
        data[game][room]["state"] = gameDict[game].turn(data[game], room, player)
        writeF(data)
clearRoom(data)
forfeitCount = 0
