# fruits = ['apple', 'mango', 'banana', 'grapes', 'papaya', '']
# for fruit in enumerate(fruits):
#    print('fruit:',fruit,)

# for _ in range(10):
#    print('apple')
#   fruits.append('apple')
# fruits.append('apple')
# print(fruits)

# while loop
#amrit = 'sitting'
#amrit == 'sitting'
#counter = 0
#while counter < 10:
#    print(counter)
#  counter = counter + 1
#   counter += 1

numbers = [1, 2, 3, 4, 5]

'''
double[1,2,3,4,5]
'''

def double(numbers: list):
    results = []
    for numbers in numbers:
       results.append(numbers * 2)

    print(results)

print(double([1,2,3]))

'''
count words if given a string, should count & return the numbers of words
5
'''

def count_words(pharse):

    print(len(pharse.split()))

count_words('Hi my name is amrit')

'''
create a function that given a list of numbers, it can return their  sum

sum_list([1, 2,3])
6

'''
def sum_list(numbers: list[int]):
   count = 0
 #  for numbers in numbers

count = 0
numbers = [1, 2, 3, 4]
count += numbers[0]
count += numbers[1]
count += numbers[2]
count += numbers[3]





