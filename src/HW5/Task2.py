# Get the key of a minimum value from the following dictionary.

def min_key(dict):
    min_value = 10000
    min_key = None
    for k, v in dict.items():
        if v < min_value:
            min_value = v
            min_key = k
    return min_key


dict = {
    'Physics': 82,
    'Math': 65,
    'History': 75
}
print(min_key(dict))
