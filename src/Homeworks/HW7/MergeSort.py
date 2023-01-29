def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return
    mid = int(n / 2)
    arr1 = [arr[i] for i in range(mid)]
    arr2 = [arr[i] for i in range(mid, n)]
    merge_sort(arr1)
    merge_sort(arr2)
    __merge(arr, arr1, arr2)


def __merge(arr, arr1, arr2):
    i = 0
    j = 0
    while i + j < len(arr):
        if j == len(arr2) or (i < len(arr1) and arr1[i] < arr2[j]):
            arr[i + j] = arr1[i]
            i += 1
        else:
            arr[i + j] = arr2[j]
            j += 1


arr = [5, 2, 6, 82, 2, 7, 1, 67, 97]
merge_sort(arr)
print(arr)