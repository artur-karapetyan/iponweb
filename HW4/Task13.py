# Ռոբոտը կանգնած է ուղղանկյուն ցանցի վրա և ներկայումս գտնվում է կետում (X0,
# Y0): Կոորդինատները ամբողջ թիվ են։ Այն ստանում է N հեռակառավարման
# հրամաններ: Յուրաքանչյուր հրաման մեկն է՝ վեր, վար, ձախ, աջ: Ճիշտ հրաման
# ստանալուց հետո ռոբոտը մեկ միավոր է տեղափոխում տվյալ ուղղությամբ։ Եթե
# ռոբոտը սխալ հրաման է ստանում, նա պարզապես անտեսում է այն: Որտե՞ղ է
# գտնվելու ռոբոտը բոլոր հրամաններին հետևելուց հետո:


def coordinate(str):
    x = 0
    y = 0

    for c in str:
        if c == 'U':
            y += 1
        elif c == 'D':
            y -= 1
        elif c == 'L':
            x -= 1
        elif c == 'R':
            x += 1

    return x, y


print(coordinate("DRRRUULRDDDDDRL"))
