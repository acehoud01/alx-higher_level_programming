#!/usr/bin/python3

def weight_average(my_list=[]):
    avarage = 0
    sumWeight = 0
    sumScore = 0
    if (len(my_list) <= 0):
        return (0)
    for item in my_list:
        score, weight = item
        sumWeight += weight
        sumScore += score * weight
    return sumScore / sumWeight
