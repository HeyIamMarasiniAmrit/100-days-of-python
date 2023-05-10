# create a program capable of displaying question to the user like KBC.
question =[ [" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],
[" which language was used to create fb?", "python", "french", "javascript","Php", "NOne", 4],

]
levels = [1000, 2000, 3000, 40000, 5000, 10000, 30000, 40000, 50000, 1600000, 200000, 6700000, 1000000, 600000, 100000000]
money = 0
for i in range(0, len(question)):
    question = question[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a.{question[i][1]}   b.{question[i][2]}")
    print(f"c.{question[i][3]}  d.{question[i][4]}")
    reply = int(input("Enter your answer(1-4) or 0 to quit:\n"))
    if(reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break
print("your take home money is {money}")