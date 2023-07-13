def merge_sort_practice(arr):
    mid = len(arr) // 2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    merge_sort_practice(arr1)
    merge_sort_practice(arr2)

    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] == arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
