import json
import time
from games import ttt, c4, rps, bts, hm, chat


game = "Selection"
forfeitCount = 0
player = 0
finished = False
ready = False
room = -1
gameDict = {
    "Tic Tac Toe": ttt,
    "Connect 4": c4,
    "Rock Paper Scissors": rps,
    "Battleship": bts,
    "AI Battleship": bts,
    "Hangman": hm,
    "Chat": chat,
}


class ReadSquares:
    def title():
        print(
            "  _____ _____ _    _               _____   _____          _____  ______ "
        )
        print(
            " / ____/ ____| |  | |        /\   |  __ \ / ____|   /\   |  __ \|  ____|"
        )
        print(
            "| (___| (___ | |__| |       /  \  | |__) | |       /  \  | |  | | |__   "
        )
        print(
            " \___ \\\\___ \|  __  |      / /\ \ |  _  /| |      / /\ \ | |  | |  __|  "
        )
        print(
            " ____) |___) | |  | |     / ____ \| | \ \| |____ / ____ \| |__| | |____ "
        )
        print(
            "|_____/_____/|_|  |_|    /_/    \_\_|  \_\\\\_____/_/    \_\_____/|______|"
        )

    def all(data):
        numRooms = [0, 0, 0, 1]
        waiting = ["_____", "_____", "Ready", "_____"]
        for p in data["Tic Tac Toe"]:
            if p["pop"] != "full":
                numRooms[0] += 1
            if p["pop"] == "waiting":
                waiting[0] = "Ready"
        for p in data["Rock Paper Scissors"]:
            if p["pop"] != "full":
                numRooms[1] += 1
            if p["pop"] == "waiting":
                waiting[1] = "Ready"
        for p in data["Hangman"]:
            if p["pop"] != "full":
                numRooms[2] += 1

        line1 = [
            "     ___________             ____________             ____________",
            "    |  Tic Tac  |           | Rock Paper |           |     AI     |",
            "    |    Toe    |           |  Scissors  |           | Battleship |",
            "    |  {} Rooms  |           |  {} Rooms   |           |   ∞ Rooms  |".format(
                numRooms[0], numRooms[1]
            ),
            "    |___{}___|           |___{}____|           |____Ready___|".format(
                waiting[0], waiting[1]
            ),
        ]
        line2 = [
            "                 ___________              ___________",
            "                |  Hangman  |            |   Chat☏   |",
            "                |           |            |           |",
            "                |  {} Rooms  |            |  {} Rooms  |".format(
                numRooms[2], numRooms[3]
            ),
            "                |___{}___|            |___{}___|".format(
                waiting[2], waiting[3]
            ),
        ]
        for line in range(len(line1)):
            print(line1[line])
        for line in range(len(line2)):
            print(line2[line])

    def ttt(data):
        numRooms = 0
        waiting = "_____"
        for p in data["Tic Tac Toe"]:
            if p["pop"] != "full":
                numRooms += 1
            if p["pop"] == "waiting":
                waiting = "Ready"
        box = [
            " ___________",
            "|  Tic Tac  |",
            "|    Toe    |",
            "|  {} Rooms  |".format(numRooms),
            "|___{}___|".format(waiting),
        ]
        for line in range(len(box)):
            print(box[line])

    def rps(data):
        numRooms = 0
        waiting = "_____"
        for p in data["Rock Paper Scissors"]:
            if p["pop"] != "full":
                numRooms += 1
            if p["pop"] == "waiting":
                waiting = "Ready"
        box = [
            " ____________",
            "| Rock Paper |",
            "|  Scissors  |",
            "|  {} Rooms   |".format(numRooms),
            "|___{}____|".format(waiting),
        ]
        for line in range(len(box)):
            print(box[line])

    def bts():
        box = [
            " ____________",
            "|     AI     |",
            "| Battleship |",
            "|   ∞ Rooms  |",
            "|____Ready___|",
        ]
        for line in range(len(box)):
            print(box[line])


def readF():
    try:
        with open("data.txt") as json_file:
            data = json.load(json_file)
        return data
    except:
        return readF()


def writeF(new):
    try:
        with open("data.txt", "w") as json_file:
            json.dump(new, json_file)
    except:
        writeF(new)


def checkTurn(game, room, player):
    data = readF()
    if game == "Hangman":
        return True, data[game][room]["state"]
    return (int(data[game][room]["state"][0]) == player), data[game][room]["state"]


def checkReady(game, room):
    data = readF()
    return data[game][room]["pop"] == "full"


def chooseGame(data):
    room = ""
    while True:
        print("")
        choice = input("Please pick a game listed: ")
        if choice == "Battleship" or choice == "AI Battleship":
            return "Battleship", 0, 1, data
        if choice == "Chat":
            return "Chat", 0, 1, data
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
    if game == "Hangman":
        data[game][room]["pop"] = "waiting"
    else:
        data[game][room]["pop"] = "empty"
    writeF(data)


# Open The JSON, read it, then close
data = readF()

# Print a UI square of data for each game
ReadSquares.title()
ReadSquares.all(data)

# Transition from selection screen to a game
game, room, player, data = chooseGame(data)
room = 1 + int(room)
writeF(data)

print("You are in room {} for {}".format(room, game))
print("Waiting for match...")
print(
    "If you are in queue 3 minutes, you will be dropped and must re-enter\nThe same is true if you are inactive in a game for 3 minutes"
)
# Wait in queue for 3 minutes or until joined
while not ready and forfeitCount < 1800:
    time.sleep(0.1)
    forfeitCount += 1
    ready = checkReady(game, room)
if ready:
    forfeitCount = 0
else:
    clearRoom(data)
gameDict[game].showBoard()
# Play game until won or forfeited
while not finished and forfeitCount < 1800:
    time.sleep(0.1)
    forfeitCount += 1
    checker, data[game][room]["state"] = checkTurn(game, room, player)
    for i in gameDict[game].playerList:
        if gameDict[game].winCheck(i, data[game][room]["state"]):
            gameDict[game].printSquare(data[game][room]["state"])
            finished = True
    if checker and not finished:
        forfeitCount = 0
        if game == "Battleship" or game == "AI Battleship":
            finished = True
            gameDict[game].turn()
        else:
            data[game][room]["state"] = gameDict[game].turn(data[game], room, player)
            writeF(data)
        # if gameDict[game].winCheck(
        #     gameDict[game].playerList[player - 1], data[game][room]["state"]
        # ):
        #     gameDict[game].printSquare(data[game][room]["state"])
        #     finished = True
time.sleep(0.5)
input("Press enter to quit.")
clearRoom(data)
forfeitCount = 0
