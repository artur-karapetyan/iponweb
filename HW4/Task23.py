# You are given an array of strings names, and an array heights that consists of distinct
# positive integers. Both arrays are of length n. For each index i, names[i] and heights[i]
# denote the name and height of the ith person. Return names sorted in descending
# order by the people&#39;s heights.


def sort(names, heights):
    temp = []
    for i in range(len(names)):
        temp.append((heights[i], names[i]))

    n = len(temp)
    while n > 1:
        for i in range(n - 1):
            if temp[i][0] < temp[i + 1][0]:
                temp[i], temp[i + 1] = temp[i + 1], temp[i]
        n -= 1

    names = [name for height, name in temp]
    return names


names = ['Mary', 'John', 'Emma']
heights = [180, 165, 170]
print(sort(names, heights))
