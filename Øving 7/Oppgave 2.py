__author__ = 'Morten Stulen'

import math

#inputNumber = int(input("Skriv inn et tall: "))

def is_prime(number):
    if number % 2 == 0 and number > 2:
        return False
    for i in range(3, int(math.sqrt(number)+1), 2):
        if number % i == 0:
            return False
    return True
#print(is_prime(inputNumber))

def seperate(list_numbers, threshold):
    list_numbers_smaller = []
    list_numbers_bigger = []
    for i in range(0, len(list_numbers)):
        if list_numbers[i] < threshold:
            list_numbers_smaller.append(list_numbers[i])
        else:
            list_numbers_bigger.append(list_numbers[i])
    return list_numbers_bigger, list_numbers_smaller
list_numbers = [1, 5, 9, 2, 10, 15, 8, 2]
threshold = 8
#print(seperate(list_numbers, threshold))

inputNumber = int(input("Skriv inn et tall her: "))

def multiplication_table(n):
    matrice = []
    for row in range(1, n + 1):
        list = []
        for col in range(1, n+1):
            list.append(row*col)
        matrice.append(list)
    return matrice
print(multiplication_table(inputNumber))








