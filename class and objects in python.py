class person:
    name = "Harry"
    occupation = "software developer"
    networth = 10
    def info(self):
      print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "Subham"
b.name = "Nikita"
a.occupation = "Accountant"
b.occupation = "HR"
#print(a.occupation)
a.info()
b.info()
c.info()