__author__ = 'enstulen'
import math
radius = float(input("Hva er radiusen på kulen?"))
overflaten = (4*radius*radius*math.pi)
volumet = ((4*radius**3*math.pi)/3)
print("Overflaten til kulen er", ("{:.2f}".format(overflaten)))
print("Volumet til kulen er", ("{:.2f}".format(volumet)))
