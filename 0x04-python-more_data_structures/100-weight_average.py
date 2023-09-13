#!/usr/bin/python3
def weight_average(my_list=[]):
    pro = 1
    sume = 0
    sum1 = 0
    if not my_list:
        return 0
    for i in my_list:
        sum1 += i[-1]
        for j in i:
            pro *= j
        sume += pro
        pro = 1
    return sume / sum1
