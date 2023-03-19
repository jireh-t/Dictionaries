heroes = {
    "MAT":
        {"Name": "Materdon",
         "Power": "Flight",
         "Strength": 5,
         "Speed": 12},
    "ORA":
        {"Name": "Orasy",
         "Power": "X-ray vision",
         "Strength": 2,
         "Speed": 8}
}

for hero_id, hero_info in heroes.items():
    print(f"\nHero ID: {hero_id}")

    for key in hero_info:
        print(f"{key}: {hero_info[key]}")
