hero_0 = {
    "Name": "Materdon",
    "Power": "Flight",
    "Strength": 5
}

print(hero_0)

hero_0["Speed"] = 12
print(hero_0)

hero_0["Strength"] = 6
print(hero_0)

popped_item = hero_0.pop("Power")
print(hero_0)
print(popped_item)
