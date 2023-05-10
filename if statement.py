num =input("Enter a number: ")
num=int(num)
if num%2==0:
    print("Number is even")
else:
    print("number is odd")

#items = 4==4
#items = 4!=4
#items = 4>4
#print(items)

Nepali = ["samosa", "daal", "naan"]
chines = ["egg role", "pot sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]
dish = input("Enter a dish name:")
if dish in Nepali:
    print("Nepali")
elif dish in chines:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("Based on little knowledge i have i dont know which cuision is", dish)

