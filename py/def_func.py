# -*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
    tmp = b*b - 4*a*c
    if a == 0:
        x = -c/b
    else:
        if tmp >= 0:
            x1 = (-b + math.sqrt(tmp))/(2*a)
            x2 = (-b - math.sqrt(tmp))/(2*a)
            return(x1, x2)
        else:
            return('无解')