# -*- coding: utf-8 -*-
"""
Updated March 17,2022
Updated Sept 8, 2018
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: jrr
@author: rk
@author: HT
"""

def classifyTriangle(a, b, c):

    if a >= 200 or b >= 200 or c >= 200:
        return 'InvalidInput'

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int)) or not(isinstance(b,int)) or not(isinstance(c,int)):
        return 'InvalidInput'

    # checks for false/true as they extend int in python but won't work here
    if a is False or b is False or c is False:
      return 'InvalidInput'
    if a is True or b is True or c is True:
      return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == a and c == b:
        return 'Equilateral'
    # have to do this for all three sides as we don't know which is the hypotenuse
    if round(a ** 2 + b ** 2) == round(c ** 2):
        return 'Right'
    if round(b ** 2 + c ** 2) == round(a ** 2):
        return 'Right'
    if round(c ** 2 + a ** 2) == round(b ** 2):
        return 'Right'
    if (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    return 'Isoceles'
