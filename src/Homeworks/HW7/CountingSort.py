def counting_sort(arr):
    n = len(arr)
    answer = [0] * n

    max_value = arr[0]
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]

    count = [0] * (max_value + 1)

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        answer[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(n):
        arr[i] = answer[i]


arr = [5, 2, 6, 82, 2, 7, 1, 67, 97]
counting_sort(arr)
print(arr)
