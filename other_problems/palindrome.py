import unittest


def is_palindrome(word):
    head = 0
    tail = len(word) - 1
    while head < tail:
        if word[head] != word[tail]:
            return False
        head += 1
        tail -= 1
    return True


class TestPalindrome(unittest.TestCase):
    palindrome_testcases = [
        ("radar", True),
        ("dragon", False),
    ]

    def test_palindrome(self):
        for testcase, expected in self.palindrome_testcases:
            assert(is_palindrome(testcase) == expected)

unittest.main()
