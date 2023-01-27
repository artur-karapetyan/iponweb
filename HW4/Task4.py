# Գրել ֆունկցիա, որը տրված բնական թվի համար կստուգի, արդյոք այն
# կատարյալ թիվ է, թե ոչ։

def check(n):
    list = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)

    sum = 0
    for i in list:
        sum += i

    if sum == n:
        return True
    else:
        return False


print(check(6))
print(check(12))
