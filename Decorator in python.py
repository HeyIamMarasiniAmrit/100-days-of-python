def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("Thanks for using this function")
        return mfx

@greet
def hello():
    print("Hello world")

def add(a, b):
    print(a + b)

#greet(hello)()
hello()

add(1, 3)