a = True
print(a:="false")

numbers = [1, 2, 3, 4, 5, 6]

while (n := len(numbers)) >0:
    print(numbers.pop())


foods = list()
while(food := input("what food do you like?:"))!="quit":
    foods.append(food)
