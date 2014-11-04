__author__ = 'enstulen'

input_tall = int(input("Skriv inn et tall: "))

def main():
    fibonacci_liste = []
    for i in range(0, input_tall + 1):
        fibonacci_liste.append(fibonacci_tall(i))
    print(fibonacci_liste)

def fibonacci_tall(tall):
    fibonacci = 0
    if tall == 0:
        fibonacci = 0
    elif tall == 1:
        fibonacci = 1
    else:
       fibonacci = fibonacci_tall(tall-1) + fibonacci_tall(tall-2)
    return fibonacci

main()