class vehicle:
    def general_usage(self):
        print("general use: transporation")


class car(vehicle):
    def __init__(self):
     print("I'm car")
     self.wheels = 4
     self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")


class Motorcycle(vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels = 2
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip, racing")


c = car()
c.general_usage()
c.specific_usage()


print(isinstance(c,Motorcycle))