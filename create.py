import json

data = {}
data["Tic Tac Toe"] = []
data["Tic Tac Toe"].append({"room": "Defaults", "pop": "full", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "0", "pop": "0", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "1", "pop": "0", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "2", "pop": "0", "state": "1_________"})

data["Battleship"] = []
data["Battleship"].append({"room": "Defaults", "pop": "full", "state": "1_________"})
data["Battleship"].append({"room": "0", "pop": "full", "state": "1_________"})

data["Rock Paper Scissors"] = []
data["Rock Paper Scissors"].append({"room": "Defaults", "pop": "full", "state": "1__"})
data["Rock Paper Scissors"].append({"room": "0", "pop": "0", "state": "1__"})
data["Rock Paper Scissors"].append({"room": "1", "pop": "0", "state": "1__"})
data["Rock Paper Scissors"].append({"room": "2", "pop": "0", "state": "1__"})

with open("data.txt", "w") as outfile:
    json.dump(data, outfile)
