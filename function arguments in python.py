# def average(a=1, b=2):
#    print("The average is ", (a + b)/2)



# average(4, 6)
# average(1,5)

#def name(fname, mname = "jhon", lname = "Whatson"):
  #  print("Hello", fname, mname, lname)


 # name("Amy")
 # keyword

# def average( f, h, l=1):
#    print("The average is", (f + h + l) / 2)


# average(5, 6)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        print("average is: ", sum/len(numbers))



average(5, 6)
