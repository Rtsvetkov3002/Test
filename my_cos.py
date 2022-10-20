#!/usr/bin/env python3
'''
my_cos
'''
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

ITERATIONS = 20

def my_cos(arg):

    """
    Вычисление косинуса при помощи частичного суммирования
    ряда Тейлора для окрестности 0
    """
    x_pow = arg**0
    multiplier = 1
    partial_sum = 1
    for iteration in range(1, ITERATIONS):
        x_pow *= arg**2 # В цикле постепенно считаем степень
        multiplier *= -1 / (2*iteration) / (2*iteration-1) # (-1)^n и факториал
        partial_sum += x_pow * multiplier

    return partial_sum

vs = np.vectorize(my_cos)
print(my_cos, vs)

angles = np.r_[-16.25:16.25:0.01]
plt.plot(angles, np.cos(angles), linewidth=3.0, color='cyan')
plt.plot(angles, vs(angles), linewidth=1.0, color='black')
plt.show()
