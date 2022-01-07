"""
This program calculates the area of a shape
Author: Larz Engquist
"""

print "It has begun"

option = raw_input('What shape do you need the area of? (C ot T): ')

if option.upper() == "C" :
  radius = float(raw_input("Enter radius: "))
  area = (radius ** 2) * 3.141592653
  print area
elif option.upper() == "T" :
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = (base * height) * 0.5
  print area
else:
  print "Invalid shape choice" 

print "Thank's for using, goodbye"  
