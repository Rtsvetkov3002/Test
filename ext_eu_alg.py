#!/usr/bin/env python3
"""
Extended Euclidian Algorythm
"""
# -*- coding: utf-8 -*-

def lin_gcd(input_a, input_b):
    """
    Linear representation of gcd
    """
    if input_a == 0:
        gcdiv = input_b
        base_x = 0
        base_y = 1
        return (gcdiv, base_x, base_y)
    div, sub_x, sub_y = lin_gcd(input_b % input_a, input_a)
    return (div, sub_y - (input_b // input_a) * sub_x, sub_x)

sample_a = int(input())
sample_b = int(input())

gcd, coef_x, coef_y = lin_gcd(sample_a,sample_b)
print(gcd, "=", coef_x, "*", sample_a, "+", coef_y, "*", sample_b)
