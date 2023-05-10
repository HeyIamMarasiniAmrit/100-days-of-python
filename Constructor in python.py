class person:

   def __init__(self, n, o):
    print("Hey i am a person")
    self.name = n
    self.occ = o


    def info(self):
       print(f"{self.name} is a {self.occ}")

a = person("Harry", "Developer")
b = person("Divya", "HR")
a.info()
b.info()
#print(a.name)
#a.name = "Divya"
#a.occ = "HR"
#a.info()