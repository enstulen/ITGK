__author__ = 'enstulen'
def main():
    f = float(input("Skriv inn temperaturen i fahrenheit: "))
    f_converted = f*(5/9)-(160/9)
    print("Temperaturen i celcius er:", f_converted)
    return
main()
