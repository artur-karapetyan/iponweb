# Գրեք Python ֆուկցիա որը ստանում է tuple և ցանկացաց տիպի օբյեկտ և ավելացնում
# է ստացած արժեքը tuple մեջ։


def add(t, obj):
    return t + (obj,)


tup = (1, 2, 'hello')
print(add(tup, 'hi'))
