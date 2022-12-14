#!/usr/bin/env python3
"""
not missing docstring
"""

# -*- coding: utf-8 -*-

import math  # подключение библиотеки math
import numpy  # подключение библиотеки numpy
import matplotlib.pyplot as mpp  # подключение библиотеки Matplotlib, переименование её в mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':  # если файл запущен напрямую (не как подключенный модуль):
    arguments = numpy.arange(0, 200, 0.1)  # создает массив из чисел [0, 200) с шагом 0.1
    mpp.plot(  # строит график:
        arguments,  # берет числа из созданного ранее массива
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # и считает значения <- этой функции
    )
    mpp.show()  # открывает окошко с графиком

