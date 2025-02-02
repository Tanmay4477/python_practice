# read and write json file in python

import json

with open('order_id.json', 'r') as file:
    data = json.load(file)

print(data["order_id"])

data["order_id"] += 2

with open('order_id.json', 'w') as file:
    json.dump(data, file)

