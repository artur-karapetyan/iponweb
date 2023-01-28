# Գրել ֆունկցիա, որը տրված 2 բնական թվերի համար կվերադարձնի նրանց
# ամենափոքր ընդհանուր բազմապատիկը։

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def multiple(a, b):
    return (a * b) / gcd(a, b)


print(multiple(5, 11))
