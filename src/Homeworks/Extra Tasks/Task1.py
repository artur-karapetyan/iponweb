# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that:
# ● i != j,
# ● abs(i - j) &lt;= indexDiff.
# ● abs(nums[i] - nums[j]) &lt;= valueDiff, and
# Return true if such pair exists or false otherwise.

def pair(nums, indexDiff, valueDiff):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) <= indexDiff and abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False


nums = [1, 5, 9, 1, 5, 9]
indexDiff = 2
valueDiff = 3
print(pair(nums, indexDiff, valueDiff))
