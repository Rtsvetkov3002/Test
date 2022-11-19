#!/usr/bin/env python3
"""
Prime check
"""
# -*- coding: utf-8 -*-

sample = int(input())
orig_sample = sample

def prime_check(input_sample,input_orig_sample):
    """
    Prime check
    """
    factorial = 1
    while input_sample!=1:
        input_sample = input_sample-1
        factorial = input_sample*factorial

    if factorial%input_orig_sample == 0:
        return False

    return True

print(prime_check(sample,orig_sample))
