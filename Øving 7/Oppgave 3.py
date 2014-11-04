__author__ = 'Morten Stulen'
#a)
# string1 = input("Skriv inn streng her: ")
# string2 = input("Skriv inn andre streng her: ")
#
# def compare_strings(string1, string2):
#     string1 = list(string1)
#     string2 = list(string2)
#
#     if len(string1) != len(string2):
#         return False
#
#     for i in range(len(string1)):
#         try:
#             if string1[i] == string2[i]:
#                 continue
#             else:
#                 return False
#         except:
#             return False
#     return True
#
# print(compare_strings(string1, string2))

#b)
# string = input("Skrv inn en streng her: ")
# def reverse_string(string):
#     newstring = ""
#     for i in range(len(string)-1, -1, -1):
#         newstring += string[i]
#     return newstring
# print(reverse_string(string))

# def reverse(string):
#     new = ""
#     for i in string:
#         new = i + new
#     return new
# print(reverse("Morten"))


#c)
# string = input("Skriv inn en streng her: ")
# def palindrom(string):
#     reversed_string = ""
#     for i in range(len(string)-1, -1, -1):
#         reversed_string += string[i]
#     if string == reversed_string:
#         return True
#     else:
#         return False
# print(palindrom(string))

#d)
string1 = input("Skriv inn streng her: ")
string2 = input("Skriv inn andre streng her: ")

def include_string(string1, string2):
    position = string1.find(string2)
    if position >= 0:
        return position
    else:
        return False
print(include_string(string1, string2))