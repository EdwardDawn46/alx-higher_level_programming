#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = []
    for num in my_list:
        if num not in unique_list:
            unique_list.append(num)
    return sum(unique_list)
