__author__ = 'Morten Stulen'


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

ukedager = [0, 1, 2, 3, 4, 5, 6]
# for i in range(1900, 1919):
#         if is_leap_year(i) == True:
#             print("skuddar")
#         elif is_leap_year(i) == False:
#             print("ikke skuddar")
#         else:
#             print()



def weekday_newyear(year):
    if (year-1900) % 7 == 0:
        return 0
    elif (year-1900) % 7 == 1:
        return 1
    elif (year-1900) % 7 == 2:
        return 2
    elif (year-1900) % 7 == 3:
        return 3
    elif (year-1900) % 7 == 4:
        return 4
    elif (year-1900) % 7 == 5:
        return 5
    elif (year-1900) % 7 == 6:
        return 6
print(weekday_newyear(1912))





