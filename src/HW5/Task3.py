# Write a Python program to copy the contents of a file to another file

def copy(file1, file2):
    with open(file1, 'r') as file1, open(file2, 'w+') as file2:
        file2.write(file1.read())


copy('File To Copy.txt', 'file.txt')
