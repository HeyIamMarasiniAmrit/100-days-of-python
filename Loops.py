##i = 1
#while i < 3:
#    print("Hello")
#    i = i + 1

#for i in range(5):
 #   print("Hello")

#print("cat\n" * 3, end="")

#while True:
 #   n = int(input("whats n ?"))
 #   if n > 0:
  #      break
#for _ in range(n):
 #   print("cat")


def main():
    number = get_number()
    dog(number)

def get_number():
    while True:
        n = int(input("whats n?"))
        if n > 0:
            break
        return n

def dog(n):
    for _ in range(n):
        print('dog')


main()