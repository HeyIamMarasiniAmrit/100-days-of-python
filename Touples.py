# TUPLES
# numbers = (1, 2)
# print(numbers)
# print(type(numbers))
# print(numbers[0])

# SETS
# list1 = ['ruby', 'python', 'java']
# list2 = ['ruby', 'sql', 'js', 'c#']

# programming_languages = set(list1 + list2)

# print(things)

# print(programming_languages)
# print('js' in programming_languages)
# print('GO ' in programming_languages)

# print({1,2, 2})

'''
>>> unique['ruby', 'ruby', 'python']
'''

def unique(languages):
    return set(languages)
unique = lambda languages: list(set(languages))

print(unique(['ruby', 'ruby', 'python']))

