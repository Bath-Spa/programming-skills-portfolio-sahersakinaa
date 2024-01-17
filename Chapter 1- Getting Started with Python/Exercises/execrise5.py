
"""
Chapter 1 Exercise 5: Compute area of Circle 
#Write a Python program which accepts the radius of a circle from the user and compute the area.
"""
                   
from math import pi 
#The value of pi is imported to the program  used in the area of circle

r=float(input("Input radius of a circle"))
 # The variable r is used to store input.

print("The area of the circle with radius" , str(r) , "is:" , str(pi*r**2))
#The area is then calculated and printed (output)