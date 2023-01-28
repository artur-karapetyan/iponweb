# Գրել ֆունկցիա, որը տրված ցուցակից կջնջի տրված արժեքին հավասար բոլոր
# էլեմենտները։

def remove(n, list):
    while n in list:
        list.remove(n)


list = [1, 2, 3, 1, 4, 1, 5]
remove(1, list)
print(list)
