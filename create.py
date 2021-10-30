import json

data = {}
data["Tic Tac Toe"] = []
data["Tic Tac Toe"].append({"room": "Defaults", "pop": "full", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "0", "pop": "0", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "1", "pop": "0", "state": "1_________"})
data["Tic Tac Toe"].append({"room": "2", "pop": "0", "state": "1_________"})

with open("data.txt", "w") as outfile:
    json.dump(data, outfile)

with open("data.txt") as json_file:
    data = json.load(json_file)
    for p in data["Tic Tac Toe"]:
        print("Room Number: " + p["room"])
        print("Current Capacity: " + p["pop"])
        print("Game State: " + p["state"])
        print("")
