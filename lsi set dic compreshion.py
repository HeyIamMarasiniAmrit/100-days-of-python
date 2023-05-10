numbers = [1, 2, 3, 4, 5, 6, 7]
even = []
for i in numbers:
    if i%2 == 0:
        even.append(i)


even
[2,4,6]
even = [i for i in numbers if i%2 == 0]
even
