class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee:{self, id} is {self.name}")

class programmer(Employee):
    def showLanguage(self):
        print("The default language is python")



e = Employee("Rohan Das", 400)
e.showDetails()
e1 = Employee("ohan Das", 400)
e1.showDetails()
e2 = programmer("han Das", 400)
e2.showDetails()
e3 = Employee("haary Das", 400)
e3.showDetails()