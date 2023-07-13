import unittest

def find_pair(arr, sum):
    compliments = set()

    for num in arr:
        compliment_num = sum - num
        if num in compliments:
            return num,compliment_num
        compliments.add(compliment_num)
    return ()


class Test(unittest.TestCase):
    testcases = [
        (([1,2,3,4],6), (4,2)),
        (([1,2,3],6), ()),
    ]

    def test_find_pair(self):
        for testcase, expected in self.testcases:
            assert(find_pair(testcase[0], testcase[1]) == expected), f"Failed testcases {testcase[0]}"

unittest.main()
