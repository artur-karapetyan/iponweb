# Մուտքագրեք երեք ամբողջ թիվ: Տպեք «Տեսակավորված» բառը, եթե թվերը նշված են
# ոչ աճող կամ չնվազող հերթականությամբ, իսկ «Չտեսակավորված» հակարակ
# դեփքում:

def check(a, b, c):
    if (a >= b and b >= c) or (a <= b and b <= c):
        return 'Sorted'
    else:
        return 'Unsorted'


a = int(input())
b = int(input())
c = int(input())
print(check(a, b, c))
