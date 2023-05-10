#def cube(x):
#    return x*x*x

#print(cube(2))
#l = [1, 2, 3, 4, 6, 4, 3]
#newl = list(map(cube, l))
#print(newl)

#def filter_function(a):
   # return a>2
#newnewl = list(filter(filter_function,l))
#print(newnewl)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
numbers = [ 4, 5]
def mysum(x, y):
    return x + y
sum = reduce (mysum, numbers)
print(sum)
