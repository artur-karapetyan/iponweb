def insertion(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


arr = [5, 2, 6, 82, 2, 7, 1, 67, 97]
insertion(arr)
print(arr)
