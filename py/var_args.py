# -*- coding: utf-8 -*-

def product(n, *args):
    value = 1
    for i in args:
        if isinstance(i, (int, float)):
            value *= i
    return n * value