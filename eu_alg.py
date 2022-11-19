#!/usr/bin/env python3
"""
Euclidian algorithm
"""
# -*- coding: utf-8 -*-

sample_a = int(input())
sample_b = int(input())

def eu_alg(input_a,input_b):
    """
    Euclidian algorithm
    """
    if input_b == 0:
        return input_a
    if input_a == 0:
        return input_b
    while 0!=1:
        input_a = input_a%input_b
        if input_a == 0:
            return input_b
        input_b = input_b%input_a
        if input_b == 0:
            return input_a

print(eu_alg(sample_a,sample_b))
