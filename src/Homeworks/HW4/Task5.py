# Գրել ծրագիր, որը տրված թվային արժեքներով ցուցակի համար, կհաշվի նրա
# էլեմենտների գումարը։

def sum(list):
    sum = 0
    for i in list:
        sum += i

    return sum


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(list))
