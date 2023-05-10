# sharing data between two process
import multiprocessing

result = []

def calc_square( result):
    for n in numbers:
        result.append(n*n)
    print('inside process' + str(result))


if __name__ == "__main__":
    numbers = [2, 3, 5]
    result = multiprocessing.Array('i',3)
    p = multiprocessing.process(targe=calc_square, args=(numbers,))


    p.start()
    p.join()


    print('outside process' + str(result))