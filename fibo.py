#!/usr/bin/env python3
"""
Print first N fibonacci numbers
"""
#  -*- coding: utf-8 -*-
import itertools

N = 10

class Fibo:
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _Fibo_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.glob_i = 0
            self.first = 0
            self.second = 1
        
        def __next__(self):
            if self.glob_i >= N:
                raise StopIteration()
            else:
                self.first, self.second = self.second, self.first + self.second
                return self.first

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibo._Fibo_iter()

f = Fibo()

for i, f in zip(
    itertools.count(1),
    itertools.islice(f, N)
):
    print(i, f)