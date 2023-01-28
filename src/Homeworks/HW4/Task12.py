# Գրեք python ծրագիր՝ նշված թվի հաջորդ ամենափոքր պալինդրոմը գտնելու համար:
# Օրինակ 119-ի համար հաջորդ պալինդրոմը 121 է

def palindrome(n):
    return str(n) == str(n)[::-1]


def nextPalindrome(n):
    while not palindrome(n):
        n += 1
    return n


print(nextPalindrome(119))
