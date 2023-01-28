# Գրեք Python ֆուկցիա որը ստանում է tuple դարձնում է string։ Tuplex֊ի էլեմենտները
# ստրինգում պետք է բաժանված լինեն ‘-’ նշանով։


def toString(t):
    return "-".join(str(x) for x in t)


t = (1, 2, 'hello', 4)
print(toString(t))
