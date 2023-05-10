s = { 1, 2, 5, 6}
s2 = { 3, 5, 6, 7}
print(s.union(s2))
print(s, s2)
s.update(s2)

cities = {'tokyo', 'madrid', 'berlin', 'delhi'}
cities2 = {"tokyo", 'seoul', 'kabul', 'madrid'}
cities3 = cities.intersection(cities2)
cities3 = cities.symmetric_difference(cities2)
cities.remove("tokyo")
print(cities)
print(cities3)
item = cities.pop()
print(cities)
