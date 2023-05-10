#fruits = ['apple', 'banana', 'blueberry', 'orange1', 'apudef2']
#print(fruits)
# fruits.append('orange')
#print(fruits)

# indecing
#print(fruits[-1])

# Slicing
#print(fruits[0:5:-1])
#print(fruits[0:len(fruits)-1])

# Dictionary
#person = {'name': 'amrit', 'shirt': 'Black', 'laptop': 'apple'}
#print(person['name'])
#print(person['laptop'])

def networth():
    return person['assets'] - person['debt']
def introducer():
    person = {
    'name' : 'amrit',
    'shirt': 'Black',
    'laptop': 'Apple',
    'assets':  100,
    'debt': 50,
    'networth': lambda:person['assets'] - person['debth']
    }

    print(f"Hi my name is {person['name']}, I am wearing a {person['shirt']}, and the laptop i use to code is an{person['laptop']}")


introducer()