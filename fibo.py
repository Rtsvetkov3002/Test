#!/usr/bin/env python3
"""
Print first N fibonacci numbers
"""
#  -*- coding: utf-8 -*-
import itertools

N = 10
base = [1, 1, 0]

class Fibo:
    """По объектам этого класса можно итерироваться и получать 6 чисел Фибоначчи"""

    class _Fibo_iter:
        """Внутренний класс — итератор"""
        def __init__(self):
            self.i = 0
            self.glob_i = 0
            self.fibs = base
        
        def __next__(self):
            if self.glob_i >= N:
                raise StopIteration()
            else:
                if self.i == 2:
                    self.fibs[0] = self.fibs[1] + self.fibs[2]
                    j = self.i
                    self.i = 0
                    self.glob_i += 1
                    return self.fibs[j]
                if self.i  == 0:
                    self.fibs[1] = self.fibs[2] + self.fibs[0]
                    j = self.i
                    self.i += 1
                    self.glob_i +=1
                    return self.fibs[j]
                else:
                    j = self.i
                    self.fibs[2] = self.fibs[0] + self.fibs[1]
                    self.i += 1
                    self.glob_i += 1
                    return self.fibs[j]

    def __iter__(self):
        """Создать и вернуть итератор"""
        return Fibo._Fibo_iter()

f = Fibo()

for i, f in zip(
    itertools.count(1),
    itertools.islice(f, N)
):
    print(i, f)