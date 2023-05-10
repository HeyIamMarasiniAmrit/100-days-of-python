item1 = "bread"
item2 = "pasta"
item3 = "fruits"

items = ["bread", "pasta", "fruits", "veggies"]
items[0] = "chips"
print(items[0:2])
print(items[-1])
items.append("butter")
print(items)
print(items.insert(1,"butter"))
print(items)
food = ["bread", "pasta", "fruits"]
bathroom = ["shampo", "soap"]
items = food + bathroom
print(items)
print(len(items))