#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:23:58 2020

@author: Matthew
"""

#!/usr/bin/env python
#
# Name: Mathew Bechtel
# Date: 26 Jan 2020
# HW #: 6

import numpy as np
import matplotlib.pyplot as plt

print('============')
print(' Homework 6')
print('============'

# -----------
# Problem 4
# -----------

print('')
print('---------')
print('Problem 4')
print('---------')

for z in range(0, 30001, 1000):
  def P(z):
    P = 1 * np.exp(((-29 * 9.81 * z)/(8.3145 * 300))/1000)
    return P
  print(z, P(z))
