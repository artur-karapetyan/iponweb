# Write a Python program to count the frequency of words in a file

def counter(file):
    freq = {}
    with open(file, 'r') as f:
        words = f.read().split()
        for i in words:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
    return freq


file = 'Random Essay.txt'
print(counter(file))
