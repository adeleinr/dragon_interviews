import unittest

def sort_even(array: list) -> list:
    even_index = 0
    odd_index = len(array) - 1

    while even_index < odd_index:
        item = array[even_index]
        if item % 2 != 0:
            temp = array[odd_index]
            array[odd_index] = item
            array[even_index] = temp
            odd_index -= 1
        else:
            even_index += 1

    return array


def delete_duplicates_from_sorted(array: list) -> list:
    first_deleted_index = -1

    for i in range(1, len(array)):
        item = array[i]
        if item == array[i-1]:
            array[i] = 0
            first_deleted_index = i
        else:
            if first_deleted_index > 0:
                array[first_deleted_index] = item
                array[i] = 0
                first_deleted_index += 1

    return array

def sample_offline_data(array:list, sample_size:int):
    """
    Implement an algorithm that takes as input an array of distinct elements and
    a size, and returns a subset of the given size of the array elements.
    All subsets should be equally likely. Return the result in input array itself.
    """

def same_elements(arr1: list, arr2):
    " Check whether 2 arrays have the same elements"
    c1 = Counter(arr1)
    c2 = Counter(arr2)
    c1 == c2


class TestProblems(unittest.TestCase):
    sort_even_testcases = [
        ([2,3,1,6,8], [2,8,6,1,3]),
        ([10,11], [10,11]),
        ( [3,5,7], [5,7,3]),
    ]
    delete_dups_testcases = [
        ([2,3,5,5,7,77,11,17,13], [2,3,5,7,77,11,17,13,0]),
    ]

    def test_sort_even(self):
        for testcase in self.sort_even_testcases:
            assert(sort_even(testcase[0]) == testcase[1])

    def test_delete_dups(self):
        for testcase in self.delete_dups_testcases:
            output = delete_duplicates_from_sorted(testcase[0].copy())
            assert(output == testcase[1]), f"Failed for testcase {testcase[0]}, output was {output}"


unittest.main()