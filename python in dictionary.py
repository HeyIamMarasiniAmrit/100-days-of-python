dic = {
    "Harry": "Human being",
    "spoon": "Object"
}
print(dic["spoon"])

dic = {
    344: "amrit",
    566: "subham",
    45: "neha",
    345: "sham"
}
print(dic[45])

info = {"name": "karan", "age": 19, "eligible": True}
print(info)
print(info["name"])
print(info.get("eligible"))

for key in info.keys():
 print(info[key])
 print(info.values())


