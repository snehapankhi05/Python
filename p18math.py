"""
Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""

import math
n=int(input("Enter number"))
print("square root",math.sqrt(n))
print("logarithm",math.log(n))
print("sin",math.sin(n))