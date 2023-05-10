import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)


func(4)
func(2)
func(1)


t1  = threading.Thread(target = func, args=[4])
t2  = threading.Thread(target = func, args=[4])
t3  = threading.Thread(target = func, args=[4])