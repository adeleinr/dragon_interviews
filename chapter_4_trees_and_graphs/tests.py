import unittest
from tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    inorder_testcases = [
        ([1,2,3], [1,2,3]),
        ([3,1,2], [1,2,3]),
    ]
    preorder_testcases = [
        ([1, 2, 3], [1, 2, 3]),
        ([3, 1, 2], [3, 1, 2]),
    ]
    get_testcases = [
        (1, 1),
        (5, None)
    ]

    def test_inorder(self):
        for case, expected in self.inorder_testcases:
            tree = BinarySearchTree()
            for value in case:
                tree.add(value)

            assert(tree.inorder(tree._root) == expected), f"Failed for input {case}"

    def test_preorder(self):
        for case, expected in self.preorder_testcases:
            tree = BinarySearchTree()
            for value in case:
                tree.add(value)
            assert(tree.preorder(tree._root) == expected), f"Failed for input {case}"

    def test_get(self):
        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        for testcase, expected in self.get_testcases:
            assert tree.get_recursive(testcase) == expected

unittest.main()