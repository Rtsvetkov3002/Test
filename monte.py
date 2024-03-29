#!/usr/bin/env python3
"""
Monte Carlo method for Euler–Poisson integral
"""
import math
import random
import timeit

ITER = 10_000_000
def monte_euler():
    """
    Int(e**(-x**2)) = sqrt(pi), функция четная
    """
    count = 0
    X_max = 2.7 # Чем больше Х, тем больше нужно брать it
    for i in range(ITER):
        x = random.uniform(0, X_max)
        y = random.uniform(0, 1)
        eul = math.e**(-x**2)
        if (y <= eul):
            count += 1
        i += 1
    approx = 1 * X_max * count / ITER
    return approx

print((2*monte_euler())**2 - math.pi)
#print(timeit.timeit(monte_euler, number=1))  # ~55,98 ITER = 100_000_000
