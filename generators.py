#def remote_control_next():
#    yield "cnn"
#    yield "espn"

#itr = remote_control()
#itr = remote_control_next()
#print(itr)

def fib():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

for f in fib():
    if f > 55:
        break
    print(f)
