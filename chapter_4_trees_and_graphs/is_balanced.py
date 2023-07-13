import unittest

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return "value: " + self.value + "right: " + self.right + " left: " + self.left


class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return self.root

        current = self.root
        while current:
            if value >= current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left


def is_balanced(values):
    tree = Tree
    [tree.add(value) for value in values]
    return is_balanced_helper(tree.root) > -1


def is_balanced_helper(node: Node) -> int:
    if node is None:
        return 0
    left_height = is_balanced_helper(node.left)
    right_height = is_balanced_helper(node.right)

    # If left subtree is not balanced then this tree is also
    # not balanced
    if left_height == -1:
        return -1
    if right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return max(left_height, right_height)


class TestIsBalanced(unittest.TestCase):

    testcases = [(["a","b","c"], False)]

    def test_is_balanced(self):
        tree = Tree()
        tree.add(self.testcases[0][0])
        assert(tree.add(self.testcases[0][0]) == self.testcases[0][1])



