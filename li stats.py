#import statistics
#print(statistics.mean([100, 90]))
import sys
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")