## higher order function ####
# map
# filter
'''
double([1, 2, 3])
[2, 4, 6]
'''
#def double_number(number):
 #return number * 2

#print(list(map(double_number, [1, 2, 3])))
#print(list(map(lambda num: num ** 2, [1, 2, 3])))

# Filter ##

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12]
print(list(filter(lambda number:number % 2== 0, numbers)))


# List comprehesions ##
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12]
[number  for number in numbers if number % 2 == 0]

# get odd numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12]
[number  for number in numbers if number % 2 != 0]