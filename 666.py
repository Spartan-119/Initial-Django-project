# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:58:57 2021

@author: abin.varghese01
"""

arr = [1, 2, 3, 4, 5]
print(id(arr))

print()

for i in range(5):
    print(i, id(i))