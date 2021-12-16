import numpy as np
from functools import reduce
import math
from time import sleep



def step_1():
    return np.arange(1000000).reshape(100,10000)



def step_2(row):
    sleep(1)
    sum = 0
    for i in row:
        sum += math.sqrt(i * 10)
    return sum



def step_3(a, b):
    return a + b


data = step_1()
map_result = map(step_2, data)
reduce_result = reduce(step_3, map_result)
print("The result is:", reduce_result)
