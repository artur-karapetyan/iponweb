# Գրել ֆունկցիա, որը տրված թվային արժեքներով ցուցակի համար, կվերադարձնի այդ
# ցուցակի ամենամեծ էլեմենտը։

def max(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max


list = [4, 2, 1, 3, 7, 3, 2, 4, 5]
print(max(list))
