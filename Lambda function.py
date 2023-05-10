# lambda function
def sum(a, b):
    return a + b
sum2 = lambda a, b: a + b
greet =lambda greet, name: f"{greet}{name}"
#print(greet('amrit', 'marasini'))
#print(sum2(1,10))

# testing code//

#print(sum(1, 2))
#assert sum(1,2)

#assert sum(-20, 20) == 0


def test_sum():
    assert sum(1, 2) == 3
    assert sum(-20, 20) == 0
    assert sum(20, 20) == 40
    assert sum(560, 780) == 1340

    print('sum FUnction: All Tests passed (4/4)')

test_sum()