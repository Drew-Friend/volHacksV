import json

data = {}
data["Chat"] = []
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})
data["Chat"].append({"Name": "John Doe", "message": "empty"})


with open("games/log.txt", "w") as outfile:
    json.dump(data, outfile)
