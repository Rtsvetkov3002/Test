#!/usr/bin/env python3
"""
Monte Carlo method for Weierstrass function, delta ~ 0,01
"""
import math
import random
import timeit
from multiprocessing import Pool

ITERS = 100_000_000
def count_one(_):
    """
    Считаем точки под графиком
    """
    count = 0
    x = random.uniform(0, 2.7)
    y = random.uniform(0, 1)
    eul = math.e**(-x**2)
    if (y <= eul):
        count += 1
    return count

def monte_euler():
    Area = 0
    if __name__ == '__main__':
        iterable = list(range(ITERS))
        with Pool() as p:
            Area = 1 * 2.7 * sum(p.map(count_one, iterable)) / ITERS
    return Area

#print((2*monte_euler())**2 - math.pi)
print(timeit.timeit(monte_euler, number=1))
#Result: 55,98  -->  19.21 ITERS = 100_000_000
