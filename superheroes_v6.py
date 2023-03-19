hero_0 = {
    "Name": "Materdon",
    "Power": "Flight",
    "Strength": 5,
    "Speed": 12}

hero_1 = {
    "Name": "Orasy",
    "Power": "X-ray vision",
    "Strength": 2,
    "Speed": 8}

hero_list = [hero_0, hero_1]

for i in hero_list:
    print(f"{i['Name']}'s superpower is {i['Power']} and their strength "
          f"value is {i['Strength']}")
