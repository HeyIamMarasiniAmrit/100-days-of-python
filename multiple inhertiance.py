class father():
    def gardening(self):
        print("I am enjoy garding")


class mother():
    def cooking(self):
        print("I love cooking")


class child(father,mother):
    def sports(self):
        print("I enjoy sports")


c = child()
c.gardening()
c.cooking()
c.sports()