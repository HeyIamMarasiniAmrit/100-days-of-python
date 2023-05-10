import time
import multiprocessing


def calc_square(numbers):
    for n in numbers:
        print('square' + str(n*n))

def calc_square(numbers):
    for n in numbers:
        print('square' + str(n * n*n))


if __name__ == "__main__":
    arr = [2,3,8,9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))


    p1.start()


    p1.join()



    print("Done")