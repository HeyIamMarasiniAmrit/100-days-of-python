students = [
    {"name": "amrit", "House": "arghakkhan"},
    {"name": "rit", "House": "hguhan"},
    {"name": "at", "House": "argan"},
    {"name": "it", "House": "an"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
