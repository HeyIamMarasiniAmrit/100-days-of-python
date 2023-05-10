class Human:
    def __init__(self, name, o):
        self.name= name
        self.occupation = o


    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")


    def speaks(self):
        print(self.name,"says how are you?")

Tom = Human("tom crusis", 'actor')
Tom.do_work()
Tom.speaks()


maria = Human("maria sharappova","tennis player")
maria.do_work()
maria.speaks()
