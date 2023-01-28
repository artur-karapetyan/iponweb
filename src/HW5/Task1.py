# Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.

def extract(keys, dict):
    return {k: dict[k] for k in keys}


dict = {'name': 'Kelly',
        'age': 25,
        'salary': 8000,
        'city': 'New York'}

keys = ['name', 'salary']

print(extract(keys, dict))
