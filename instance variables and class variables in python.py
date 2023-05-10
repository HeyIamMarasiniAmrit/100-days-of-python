class Employee:
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        def showDetails(self):
            print(f"The name of the employee is {self.name} and the raise amount is {self.raise_amount}")
# Employee.showDetails(emp1)

emp1 = Employee("Harry")
emp1.raise_amount = 0.03
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()