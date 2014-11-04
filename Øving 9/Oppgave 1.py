__author__ = 'Morten Stulen'


def annual_value(sum_A, rent_r, year_k):
    n = 12
    list_value = []
    for i in range(0, year_k + 1):
        value = sum_A * ((1 + rent_r/n) ** (n*i))
        list_value.append(value)
        print("%s \t \t %s \n" % (i, list_value[i]))
    value = sum_A * (1 + rent_r/n) ** (n*year_k)
    return value
    #return list_value
print(annual_value(1000, 0.05, 20))

# def calculate_start_sum(wanted_end_sum):
#     if wanted_end_sum >= (annual_value(x, 0.05, 20)):
