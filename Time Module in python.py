import time

def usingwhile():
    while i<50000:
        i = i + 1
        print(i)


def usingfor():
    for i in range(500):
        print(i)

init = time.time()
usingfor()
print(time.time() - init)
init = time.time()
usingwhile()
print(time.time() - init)