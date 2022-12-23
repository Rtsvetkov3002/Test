#!/usr/bin/env python3
"""
Making fractal using turtle
"""
# -*- coding: utf-8 -*-
import turtle as tl

def draw_fractal(scale):
    """
    Algorithm for turtle
    """
    if scale >= 2:
        tl.left(120)
        tl.forward(3**(scale-1))
        draw_fractal(scale - 1)
        tl.forward(3**(scale-1))
        tl.right(120)
        tl.forward(3**(scale-1))
        draw_fractal(scale - 1)
        tl.forward(3**(scale-1))
        tl.right(120)
        tl.forward(3**(scale-1))
        draw_fractal(scale - 1)
        tl.forward(3**(scale-1))
        tl.left(120)
    else:
        tl.forward(3**(scale-1))

SCALE = 5

tl.pensize(2)
tl.speed(0)
tl.pendown()

draw_fractal(SCALE)
tl.done()
