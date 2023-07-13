# Merge two sorted arrays into one
def merge(arr1, arr2):
    result_list = []
    if not arr1 and not arr2:
        return []
    while arr1 or arr2:
        if arr1 and arr2:
            if arr2[0] <= arr1[0]:
                result_list.append(arr2.pop(0))
            else:
                result_list.append(arr1.pop(0))
        elif arr1:
            result_list.append(arr1.pop(0))
        else:
            result_list.append(arr2.pop(0))

    return result_list

print(merge([1,2,3,6,6], [1,2,2,5,7]))
print(merge([], []))
print(merge([1], []))
print(merge([], [1]))
print(merge([0,1], [1]))
