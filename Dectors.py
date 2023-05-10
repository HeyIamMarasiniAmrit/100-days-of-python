import time
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print("calc_square took")


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
        return result


array = range(1,1000)
out_square = calc_square(array)
out_cube = calc_cube(array)