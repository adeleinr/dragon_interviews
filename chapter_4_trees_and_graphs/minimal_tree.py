import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

"""
 Given a sorted (increasing order) array with unique integer elements,
 write an algorithm to create a binary search tree with minimal height.
"""
class MinBinaryTree:
    def __init__(self, values: list):
        self.root = self.build_tree(values, 0, len(values)-1)

    def build_tree(self, array:list, start:int, end:int) -> Node:
        if start > end:
            return None
        mid = (start+end) // 2 # Returns an int instead of float
        root = Node(array[mid])
        root.left = self.build_tree(array, start, mid-1)
        root.right = self.build_tree(array, mid+1, end)
        return root

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)


class TestMinimalTree(unittest.TestCase):

    min_tree_testcases=[
        ([1,2,3,4,5,6], [1,2,3,4,5,6], [4,2,1,3,5,6]), # Assumes input in sorted order
    ]

    def test_sunny_day_case(self):
        for case in self.min_tree_testcases:
            tree = MinBinaryTree(case[0])
            assert(tree.inorder(tree.root) == case[1]), f"Failed for array {case[0]}"

unittest.main()