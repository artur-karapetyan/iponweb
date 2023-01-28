# Write a Python program to read last n lines of a file

def read(file, n):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines[-n:]]


file = "file.txt"
print(read(file, 4))
