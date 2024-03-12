#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    for score, weight in my_list:
        numerator += score * weight
        denominator += weight
    return numerator / denominator
