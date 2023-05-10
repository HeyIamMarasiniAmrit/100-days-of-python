import random

class Hat:

    def __init__(self):
        self.house = ["amrit", "harry", "gulmi", "sandip", "arghkhanchi"]


    def sort(cls, name):
        print(name, "is in",random.choice(cls.house))




hat = Hat()
hat.sort("Harry")
