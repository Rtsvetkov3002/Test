#!/usr/bin/env python3
"""
Print first N fibonacci numbers
"""
#  -*- coding: utf-8 -*-
import itertools

N = 16

class Fibo:

    class _Fibo_iter:
        def __init__(self):
            self.first = 0
            self.second = 1

        def __next__(self):
                self.first, self.second = self.second, self.first + self.second
                return self.first

    def __iter__(self):
        return Fibo._Fibo_iter()

f = Fibo()

for i, f in zip(
    itertools.count(1),
    itertools.islice(f, N)
):
    print(i, f)
