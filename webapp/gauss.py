#!/usr/bin/env python3
"""
Gauss method
"""
# -*- coding: utf-8 -*-
import numpy
from numpy import array
from numpy.linalg import norm
from numpy.linalg import solve as solve_out_of_the_box

def gauss(a, b):
    """
    Gauss method
    """
    a = a.copy()
    b = b.copy()

    def forward():
        for i in range(len(a)):
            for j in range(i+1, len(a)):
                b[j] = b[j] - a[j][i] / a[i][i] * b[i]
                a[j] = a[j] - a[j][i] / a[i][i] * a[i]

    x = numpy.zeros(len(b), dtype=float)
    def backward():
        for i in range(len(a)-1, -1, -1):
            Sum = 0
            for j in range(i+1, len(a)):
                Sum += x[j]*a[i][j]
            x[i] = (b[i]- Sum)/a[i][i]
        return x

    forward()
    x = backward()
    return x

if __name__ == "__main__": #для задания modules
    a = array([
        [1.5, 2.0, 1.5, 2.0],
        [3.0, 2.0, 4.0, 1.0],
        [1.0, 6.0, 0.0, 4  ],
        [2.0, 1.0, 4.0, 3  ]
        ], dtype=float)
    b = array([5, 6, 7, 8], dtype=float)

    oob_solution = solve_out_of_the_box(a, b)
    solution = gauss(a, b)

    print(solution)
    print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))
