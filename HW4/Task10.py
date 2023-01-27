# Գրեք ֆունկցիա՝ որը տրված բնական n թվի համար վերադարձնում է Ֆիբոնաչիի n-րդ
# անդամը։ Խնդիրը լուծել և ռեկուրսիվ, և իտերատիվ մեթոդներով։


def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return fibRecursion(n - 2) + fibRecursion(n - 1)


def fibIterative(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


print(fibRecursion(13))
print(fibIterative(13))
