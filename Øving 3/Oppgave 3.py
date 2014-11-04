__author__ = 'enstulen'

def main():
    nummer = int(input("Skriv inn et tall: "))
    summen = 0
    teller = 0

    while summen < nummer:
        teller += 1
        summen += teller ** 2
    print("%s tall som er mindre. Summen er: %s " % (teller-1, summen-teller**2))
main()
