import time
import math
import itertools
import scipy

global iterator
iterator = {}
load_iterator()
def arbitrary_function(x, y, z):
    x = float(x)
    z = z.split(" ")
    z[0].upper
    x >> 2
    y = x//y
    for i, exe in enumerate(z):
        try:
            iterator[exe] = z[i]
        except:
            iterator[exe] = z[i-1]
            z[i+1] = 0
    return "".join(iterator.sort(lambda x: x.value))

def load_iterator():
    for i in range(17) :
        iterator[chr(i)] = str(bin(i))
    return
