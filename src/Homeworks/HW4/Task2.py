# Օգնեք Ratiorg-ին՝ գրելով ֆունկցիա, որը վերադարձնում է տվյալ inputString-ում
# հայտնված թվերի գումարը։
import re


def sum(str):
    list = re.findall('[0-9]+', str)
    sum = 0
    for i in range(len(list)):
        sum += int(list[i])
    return sum


print(sum(input()))
