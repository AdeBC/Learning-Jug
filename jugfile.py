from jug import TaskGenerator, mapreduce, bvalue
import numpy as np
from time import sleep
import math



def step_1():
    return np.arange(1000000).reshape(100,10000)


@TaskGenerator
def step_2(row):
    sleep(1)
    sum = 0
    for i in row:
        sum += math.sqrt(i * 10)
    return sum


@TaskGenerator
def step_3(a, b):
    return a + b


data = step_1()
map_result = mapreduce.map(step_2, data, map_step=10)
print('Map done:', bvalue(map_result))
reduce_result = mapreduce.reduce(step_3, map_result, reduce_step=10)
print("The result is:", bvalue(reduce_result))
