# set is an unorderd
basket = {"orange", "apple", "mango", "orange", "apple"}
print(type(basket))
print(basket)

a = set()
a.add(1)

a.add(2)
print(a)

numbers = [1,2,3,4,5,6]
unique_numbers=set(numbers)
print(unique_numbers)
unique_numbers.add(7)
print(unique_numbers)

fs = frozenset(numbers)
fs.add(5)

y = {"a", "b", "c"}
print(y)

x = {"m", "k", "l"}
z = x|y
print(z)