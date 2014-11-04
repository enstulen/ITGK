__author__ = 'Morten Stulen'

list = [1]
list2 = [1, 1]
list3 = [1, 1, 1]
list4 = [3, 1, 3]
list5 = [1, 2, 3, 4]
list6 = [1, 2, 3, 4, 5]
list7 = [7, 3, 8, 6, 5]
list8 = [7, 3, 1000, 3, 7]
list9 = [2, 5, 4]
def center_of_mass(pole_list):
    meters = len(pole_list)
    total_weight = 0
    weight_over_desired_weight = 0
    weight_under_desired_weight = 0
    number_of_poles = 0

    if meters == 1:
        return pole_list[0]/2

    #Desired weight
    for i in range(0, len(pole_list)):
        total_weight += pole_list[i]
    desired_weight = total_weight/2
    print("Desired weight: ", desired_weight)

    #Weight over desired weight
    for i in range(0, len(pole_list)):
        weight_over_desired_weight += pole_list[i]
        if weight_over_desired_weight > desired_weight:
            number_of_poles = i
            break
        elif weight_over_desired_weight == desired_weight:
            return weight_over_desired_weight
    #Weight under desired weight
        weight_under_desired_weight += pole_list[i]
        if weight_under_desired_weight > desired_weight:
            weight_under_desired_weight -= pole_list[i]
    print("Weight over desired weight: ", weight_over_desired_weight)
    print("Weight under desired weight: ", weight_under_desired_weight)
    print("Number of poles: ", number_of_poles)


    #Added metres
    denominator = weight_over_desired_weight - weight_under_desired_weight
    numarator = desired_weight - weight_under_desired_weight
    print("Numarator: ", numarator)
    print("Denominator:", denominator)

    extra = float(numarator/denominator)

    return(number_of_poles + extra)

print(center_of_mass(list5))

















