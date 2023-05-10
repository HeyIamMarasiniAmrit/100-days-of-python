import time
import multiprocessing

def deposit(balance):
    for i in range(100):
        time.sleep(0.001)
        balance.value = balance.value + 1
        lock.release()


def withdraw(balance):
    for i in range(100):
        time.sleep(0.01)
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.value('i', 200)
    lock = multiprocessing.lock()
    d= multiprocessing.process(target=deposit, args=(balance,))
    w = multiprocessing.process(target=deposit, args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)