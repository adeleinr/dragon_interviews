import unittest


def sorting_tuple_sums(arr):
    return sorted(arr, key=sum, reverse=True)

class TestSorting(unittest.TestCase):
    sorting_tuples_unittests = [([(2,2,1), (4,1,5)], [(4,1,5), (2,2,1)])]
    for input, expected in sorting_tuples_unittests:
        assert(sorting_tuple_sums(input) == expected), f"Failed on input {input}"


unittest.main()