# Գրեք ֆունկցիա՝ տողը հակադարձելու համար, եթե դրա երկարությունը 4-ի
# բազմապատիկ է։


def reverse(str):
    if len(str) % 4 == 0:
        return str[::-1]
    else:
        return str


str = 'Hello World!'
print(reverse(str))
