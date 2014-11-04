__author__ = 'Morten Stulen'
import math

def create_vector_list():

    # x = int(input("Forste komponent: "))
    # y = int(input("Andre komponent: "))
    # z = int(input("Tredje komponent: "))
    # list_vector = [x, y, z]

    inputNumbers = input("Skriv inn 3 kompnenter med mellomrom: ")
    inputNumbers = inputNumbers.split()

    for i in range(0, len(inputNumbers)):
        inputNumbers[i] = int(inputNumbers[i])

    return inputNumbers


def write_vector_list():
    vec1 = create_vector_list()
    print("\n" "Vektoren vec1 = (%s, %s, %s)" % (vec1[0], vec1[1], vec1[2]))
    return vec1


def scalar_multiplication(vector, scalar):
    #scalar_product2 = [x * scalar for x in vector]
    scalar_product = [vector[0] * scalar, vector[1] * scalar, vector[2] * scalar]
    return scalar_product


def calculate_vector_length(vector):
    vector_length = math.sqrt((vector[0] ** 2) + (vector[1] ** 2) + (vector[2] ** 2))
    return vector_length


def vector_multiplication(vector1, vector2):
    vector_product = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    return vector_product


def main():
    #Before scalar multiplication
    vec1 = write_vector_list()
    vector_length_before = calculate_vector_length(vec1)
    print("Vektorlengden for skalarmultiplikasjon: %.2f " % (vector_length_before))

    #After scalar multiplication
    input_scalar = int(input("\n" "Skalarproduktet: "))
    vec1 = scalar_multiplication(vec1, input_scalar)
    print("\n" "Vektoren vec1 = (%s, %s, %s)" % (vec1[0], vec1[1], vec1[2]))
    vector_length_after = calculate_vector_length(vec1)
    print("Vektorlengden etter skalarmultiplikasjon: %.2f " % (vector_length_after))

    #Comparison
    print("\n" "Forholdet er %.2f og differansen er %.2f" % (vector_length_after/vector_length_before, vector_length_after - vector_length_before))

    #Vector multiplication
    print("\n" "Skriv inn en ny vektor!")
    vec2 = create_vector_list()
    vector_product = vector_multiplication(vec1, vec2)
    print("\n" "Vektor produktet er: %d" % (vector_product))

main()