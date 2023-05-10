#f = open("funny.txt","w")
#f.write("I Love php")
#f.close()

#f= open("fuuny.txt",'r')
#print("f.read")
#f.close()

def calculate_area(base,height):
    return 1/2*(base*height)

if __name__ == "__main__":
    a = calculate_area(10,20)
    print('area: ',a)