__author__ = 'enstulen'

debug = True
def add(num1, num2):
    if debug == True:
        print("Tallene som printes ut er %s og %s" % (num1, num2))
    print(num1 + num2)

add(7,4)