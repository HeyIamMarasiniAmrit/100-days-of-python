#class ParentClass:
   # def parent_method(self):
  #      print("THis is the parent method.")

#class ChildClass(ParentClass):
   # def parent_method(self):
   #     print("Harry")
   #     super().parent_method()
  #  def child_method(self):
  #      print("This is the child method.")
   #     super(). parent_method()

#child_object = ChildClass()
#child_object.child_method()
#child_object.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer:
    def __init__(self, name, id, lang):
        self.name = name
        self.id = id
        self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = programmer("Harry", "3459", "python")
print(rohan.name)