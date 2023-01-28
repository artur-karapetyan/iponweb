# Գրեք ֆուկցիա որը ստանում է tuple տիպի օբյեկտ և վերադարձնում նոր tuple
# բաղկացած միայն առաջին tuple֊ի թվերից։


def newTuple(t):
    return tuple(x for x in t if isinstance(x, (int, float)))


print(newTuple((1, 2, 3, 'hghg', 2.4, 'dfg')))
