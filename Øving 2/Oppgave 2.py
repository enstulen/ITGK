__author__ = 'enstulen'
# a)
# 7 3
# 5 4
# 5 3
# 7 3
# b)
# Først skrives 7 og 3 ut fordi de er de første i main funksjonen som kjøres først.
# Derretter skrives 5 og 4 ut fordi miks-funksjonen kjøres i main-funksjonen etter at den har printet ut 7 og 3.
# Deretter skrives 5 og 3 ut fordi tull-funksjonen kjøres som henter de orginale verdiene til x og y som ble definert først.
# Til slutt skrives 7 og 3 ut igjen fordi du printer ut x og y verdiene som er i main-funksjonen.

x = 5
y = 3


def main():
    x = 7
    y = 3
    print(x, y)
    miks(y, x)
    tull()
    print(x, y)


def miks(x, y):
    x = 5
    y = 4
    print(x, y)


def tull():
    print(x, y)


main()