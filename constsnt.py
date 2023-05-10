class cat:
    meows = 100
    

    def meow(self):
        for _ in range(cat.meows):
            print("meow")


cat = cat()
cat.meow()