#class Employee:

#a = Employee()
# print(a.__name) cannot be accessed directly
#print(a._Employee__name) # can be aceessed indirectly

#print(a.__dir__())

class Students:
    def __init__(self):
        self._name = "Harry"

    def _funname(self):
        return "code with Harry"

class subjects(Students):
    pass

obj = Students()
obj1 = subjects()

print(obj._name)
print(obj._funname())

print(obj1._name)
print(obj1._funname())
