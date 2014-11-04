__author__ = 'enstulen'

def main():
    bil_navn = input("Navn på bilen:")
    bil_bruttopris = float(input("Bruttopris på bilen: "))
    bil_vekt = float(input("Vekt på bilen i kg: "))
    bil_hestekrefter = float(input("Hestekrefter på bilen: "))
    bil_utslipp = float(input("Utslipp fra bilen (CO2) i gram: "))
    bil_motorvolum = float(input("Motorvolum i liter: "))

    beregn_avgift(bil_navn, bil_bruttopris, bil_vekt, bil_hestekrefter, bil_utslipp, bil_motorvolum)


def beregn_avgift(bil_navn, bil_bruttopris, bil_vekt, bil_hestekrefter, bil_utslipp, bil_motorvolum):
    vekt_p = (bil_bruttopris * bil_vekt * 0.00034)
    hestekrefter_p = (bil_bruttopris * bil_hestekrefter * 0.00015)
    co2_p = (bil_bruttopris * bil_utslipp * 0.004)
    volum_p = (bil_bruttopris * bil_motorvolum * 0.00055)

    nettopris = float((bil_bruttopris + vekt_p + hestekrefter_p + co2_p + volum_p))
    print("Utsalgspris på %s vil bli %.2f" % (bil_navn,nettopris))

main()

#Ford mondeo 1.8 = Utsalgspris på Ford mondeo vil bli 369594.00
#Ford mondeo 1.0 = Utsalgspris på ford mondeo  vil bli 341893.50
#BMV M5 3.0 = Utsalgspris på BMV vil bli 1033682.00
#BMV M5 1.3 = Utsalgspris på bmw vil bli 793989.00
