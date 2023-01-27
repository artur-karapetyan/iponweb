# Ստուգեք, արդյոք 2 ցուցակները 1-քայլ ցիկլիկ են:


def check(list1, list2):
    temp = list1 * 2
    l = len(list2)
    for i in range(len(temp)):
        if list2 == temp[i: i + l]:
            return True
    return False


list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 1, 2, 3, 4, 5]
print(check(list1, list2))
