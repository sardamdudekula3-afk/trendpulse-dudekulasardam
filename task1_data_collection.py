import json

data = [
    {"title": "AI Technology", "category": "Tech", "views": 1500},
    {"title": "Cricket World Cup", "category": "Sports", "views": 2500},
    {"title": "Stock Market News", "category": "Finance", "views": 1800},
    {"title": "New Movie Release", "category": "Entertainment", "views": 2200}
]

with open("data.json", "w") as file:
    json.dump(data, file)

print("Data saved")
