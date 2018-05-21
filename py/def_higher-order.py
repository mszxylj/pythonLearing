# -*- coding: utf-8 -*-
# 高阶函数 #
# 一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。#

def add(x, y, f):
    return f(x) + f(y)

print(add(-2, 6, abs))

def addOne(x):
    return x+1

print(add(2, 6, addOne))
