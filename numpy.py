import numpy as np
import time
import sys

#l = range(1000)
#print(sys.getsizeof(5)*len(l))

#array = np.arange(1000)
#print(array.size*array.itemsize)

size = 1000

l1 = range(size)
l2 = range(size)

#a1=np.arange(size)
#a2=np.arange(size)

start = time.time()
#result = [(x + y) for x,y in zip(11,12)]
print("python list took: ",(time.time()-start)*1000)

# numpy  array
start = time.time()
#result = a1 + a2
print("numpy took: ",(time.time()-start)*1000)


