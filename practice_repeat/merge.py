def merge_sorted_arrays(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < len(arr1):
        result.extend(arr1[i:])
    elif j < len(arr2):
        result.extend(arr2[j:])
    return result



arr1 = [1,2,3,6,8,9]
arr2 = [2,2,5,6]
print(merge_sorted_arrays(arr1, arr2))
