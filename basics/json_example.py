import json  
data = {"name": "Aakash", "age": 20 }
with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json") as f:
    print(json.load(f))