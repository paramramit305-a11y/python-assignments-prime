# Q4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json".

# 1. Then load the JSON and print each city and its populations.
# 2. Ask the user for a new city & its populations - update this info in the json file.

import json

cities = {
    "Gujrat" : 50_000,
    "Mumbai" : 100_000,
    "Delhi" : 200_000
}

with open("cities.json", "w") as f:
    json.dump(cities, f)

with open("cities.json", "r") as f:
    data = json.load(f)

for city, pop in data.items():
    print(city, pop)

new_city = input("Enter new city: ")
new_pop = int(input("Enter population: "))

data[new_city] = new_pop

with open("cities.json","w") as f:
    json.dump(data, f)