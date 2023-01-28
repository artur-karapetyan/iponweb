# Euler function is return a count of numbers not great than N, which are mutualy simple with
# N.
# Example φ(6)=2, as only 1 and 5 from 1,2,3,4,5 are mutually simple with 6. Write a function
# which return count of numbers mutually simple with given N.

def phi(n):
    count = 0
    for i in range(1, n + 1):
        if gcd(n, i) == 1:
            count += 1
    return count


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(phi(6))
