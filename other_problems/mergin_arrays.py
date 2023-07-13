# In the language of your choice, write a function that takes two arrays of integers, and return an array of their intersection. Each element in the returned array must be unique, and the results can be returned in any order.

# Examples to provide:

# [3, 1, 2], [2, 1] -> [1, 2] or [2, 1]
# [1, 2, 2, 2], [2, 2] -> [2]

# [1, 2, 2, 2], [2, 2]
# [1, 2], [2]

# [], [2]
from collections import Counter


def find_intersection(arr1, arr2):
    result = []
    d1 = Counter(list(set(arr1)))
    for num in set(arr2):
        if num in d1:
            result.append(num)
    return result


print(find_intersection([3, 1, 2], [2, 1]))
print(find_intersection([1, 2, 2, 2], [2, 2]))
print(find_intersection([], [2]))
print(find_intersection([2], []))

#[1, 2, 2, 3], [1, 1, 2, 2] = > []
#[1, 1, 2, 3], [1, 2, 2]


def find_intersection_2(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if i > 0 and arr1[i - 1] == arr1[i]:
            i += 1
            continue
        if j > 0 and arr2[j - 1] == arr2[j]:
            j += 1
            continue
        if arr1[i] == arr1[j]:
            result.append(arr1[i])
            i += 1
            j += 1
    return result

















