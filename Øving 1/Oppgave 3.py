__author__ = 'enstulen'
import math


def beregn_volum(radius):
    volum = ((4 * radius * radius * radius * math.pi) / 3)
    print("Volumet til kulen med radius %s er %s" % (radius, "{:.2f}".format(volum)))



def main():
    beregn_volum(2.5)
    beregn_volum(5.0)
    beregn_volum(7.5)

main()
