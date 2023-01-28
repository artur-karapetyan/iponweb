# Ticket numbers usually consist of an even number of digits. A ticket number is considered
# lucky if the sum of the first half of the digits is equal to the sum of the second half.
# Given a ticket number n, determine if it&#39;s lucky or not. Not using: string, list, tuple, set
# types.


def isLucky(n):
    temp = n
    len = 0
    while temp > 0:
        temp //= 10
        len += 1
    half = len // 2
    firstHalf = n // 10 ** half
    secondHalf = n % 10 ** half
    firstSum = 0
    secondSum = 0
    for i in range(half):
        firstSum += firstHalf % 10
        firstHalf //= 10
        secondSum += secondHalf % 10
        secondHalf //= 10
    return firstSum == secondSum


print(isLucky(1230))
print(isLucky(239017))
print(isLucky(12345221))