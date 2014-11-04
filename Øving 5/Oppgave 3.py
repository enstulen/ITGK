__author__ = 'Morten Stulen'
while True:
    try:
        alder = int(input("Hvor gammel er du? "))
        if alder < 5 and alder >=0:
            print("Gratis")
        elif alder <= 15:
            print("10 kr")
        elif alder >= 16 and alder <= 20:
            print("20 kr")
        elif alder >= 21 and alder <= 25:
            print("30 kr")
        elif alder >= 26 and alder <= 60:
            print("40 kr")
        elif alder > 60 and alder < 130:
            print("Gratis")
        else:
            print("Skriv inn en gyldig alder")
    except ValueError:
        print("Skriv inn et heltall")


























