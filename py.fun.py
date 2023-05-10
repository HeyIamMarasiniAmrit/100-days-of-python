#nums = [25, 12, 36, 95, 14]
#print(nums[-4])
##['navin', 'kiran', 'jhon']
#values = [9.5, 'navin', 25]
#mil = []

#tup = (21, 36, 14, 25)
#print(tup[1])

#s = (22, 25, 14, 21, 5)
#print(s)
# Dictionary

# functions in python

#tom_exp_list = [2100, 3400, 3500]
#joe_exp_list = [200, 500, 700]

#total = 0
#for item in tom_exp_list:
#     total = total + item
#print("Toms total expense:", total)


#total = 0
#for item in joe_exp_list:
#    total = total + item
#print("joes total expense:", total)

def calculate_total(exp):
    total = 0
    for item in exp:
        total = total + item
    return total

tom_exp_list = [2100, 3400, 3500]
joes_exp_list = [200, 500, 700]

toms_total = calculate_total(tom_exp_list)
joes_total= calculate_total(joes_exp_list)

print("Toms total expense:", toms_total)
print("joes total expense:", joes_total)


def sum(a,b):
    total = a + b
    return total


n= sum(5,6)
print("total:",n)