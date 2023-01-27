# Գրեք ֆունկցիա որը կվերադարձնի տրված թվային արժեքներով ցուցակի բոլոր
# էլեմենտների արտադրյալը։

def mult(list):
    answer = 1
    for i in list:
        answer *= i

    return answer


list = [1, 2, 3, 4, 5, 6]
print(mult(list))
