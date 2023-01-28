# Գրել ծրագիր, որը ստանւմ է թիվ, գտեք առավելագույն թիվը, որը կարող եք ստանալ՝
# ջնջելով տվյալ թվի ուղիղ մեկ թվանշանը:

def remove(n):
    numberString = str(n)
    answer = 0
    for i in range(len(numberString)):
        temp = int(numberString[:i] + numberString[i + 1:])
        if temp > answer:
            answer = temp
    return answer


print(remove(152))
print(remove(1001))
