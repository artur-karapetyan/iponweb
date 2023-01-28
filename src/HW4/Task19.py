# Գրեք Python ֆուկցիա որը ստանում է list և պետքա գտնել նրա երկարությունը առանց
# len() ֆունկցիա֊ի օգտագորձմամբ։


def length(l):
    count = 0
    for i in l:
        count += 1
    return count


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(length(l))
