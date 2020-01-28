#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:23:58 2020

@author: Matthew
"""

# While this is a cleaner version of HW 6, I am over making this, so that we can use it as a template for future labs/HW
#!/usr/bin/env python
#
# Name: Mathew Bechtel
# Date: 26 Jan 2020
# HW #: 6

import numpy as np
import matplotlib.pyplot as plt

# List object containing the function names of all HW problems
problemFunctions = [prob1, prob2, prob3, prob4]

# Problem num 4
def prob4():
  for z in range(0, 30001, 1000):
    P = 1 * np.exp(((-29 * 9.81 * z)/(8.3145 * 300))/1000)
    print(z, P)

# Prints the problem number (passed as int)
def problemPrint(prob):
  print('')
  print("---------")
  print("Problem %d" % (prob))
  print("---------')

# Function first runs funtion to print problem number, then grabs correct function from list to run
def questionNum(numb):
  problemPrint(numb)
  problemFunctions[numb]()
  
# Prints the homework version, modify by changing the int in the main function
def homeworkNumPrint(hw):
  print("============")
  print(" Homework %d" % (hw))
  print("============")
        
def main():
  #Change the number for the assignment number
  homeworkNumPrint(6)
  numberProbs = problemFunctions.size()
# Uncomment one of the two, 1st for testing/running specific problem(s), 2nd for running all problems
# for i in range(1, numberProbs):
  for i in range(4, 4):
    questionNum(i)
    
      
if __name__ == "__main__":
      main()
