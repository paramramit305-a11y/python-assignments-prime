import json

# with open("data.json", "r") as f:
#     data = json.load(f)

# print(data)

data = {
    "name":"Amit",
    "city": "palanpur"
}

with open("data.json","w") as f:
    json.dump(data, f, indent=4)
