def binary_search(arr, value):
    sorted_arr = sorted(arr)
    return binary_search_helper(sorted_arr, value)


def binary_search_helper(arr, value):
    mid = len(arr) // 2
    if arr[mid] == value:
        return True

    binary_search(arr[:mid], value)
    binary_search(arr[mid+1:], value)
    return False


print(binary_search([1,4,6,7,8,9], 6))

