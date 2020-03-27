#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python
#
# Name: Mathew Bechtel
# Date: [date]
# HW #: [number]

import numpy as np
import matplotlib.pyplot as plt

# List object containing the function names of all HW problems
problemFunctions = [prob1, prob2, prob3, prob4]

# Problem num x
def prob1():
  print("Do something")

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
# Change the number for the assignment number
  homeworkNumPrint(6)
# Gets the number of problems in the assignment for the for loop
  numberProbs = problemFunctions.size()
# Uncomment one of the two, 1st for testing/running specific problem(s), 2nd for running all problems
#  for i in range(1, numberProbs):
#  for i in range(1, 1):
  questionNum(i)
    
# Good practice to include this, for preventing bad coding of bugs when calling main functions from imported libraries
if __name__ == "__main__":
  main()
