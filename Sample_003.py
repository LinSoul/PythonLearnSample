#!/usr/bin/python
# coding: utf-8

import math

__author__ = 'Magic'


for i in range(100000):
    x = int(math.sqrt(i + 100))
    y = int(math.sqrt(i + 268))
    if (x*x == i + 100) and (y*y == i + 268):
        print i

