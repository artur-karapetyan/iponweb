# Տրված է թվաբանական պրոգրեսիայի առաջին և երկրորդ անդամները։ Տրված n֊ի
# համար, վերադարձնել այդ պրոգրեսիայի n֊րդ անդամը։

def arithmetic(first, second, n):
    temp = second - first
    answer = second
    for i in range(2, n):
        answer += temp
    return answer


first = float(input())
second = float(input())
n = int(input())
print(arithmetic(first, second, n))
