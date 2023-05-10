def calculateGmean(a, b):
    mean=(a *b)/(a+b)
    print(mean)

def isGreater(a, b):
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater or equal")

a = 9
b = 8
isGreater(a, b)
# if(a>b):
#    print("first number is greater")
# else:
  #  print("second number is greater or equal")
# gmean1 = (a *b)/(a +b)
# print(gmean1)
calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
# if(c>d):
 #   print("first number is greater")
# else:
#    print("second number is greater or equal")
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmean(c, d)