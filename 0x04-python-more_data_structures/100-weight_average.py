#!/usr/bin/python3
def weight_average(my_list=[]):
    score = 0
    total = 0
    for i in my_list:
        score += i[0] * i[1]
        total += i[1]
    return score / total
