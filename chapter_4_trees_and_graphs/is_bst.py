import unittest
from binarytree import Node


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        return "value: " + self.value + " right: " + self.right + " left: "+ self.left

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder((node.right))

class Tree:
    def __init__(self, node=None):
        self.root = node

    def add(self, values: list) -> bool:
        for value in values:
            if self.root is None:
                self.root = Node(value)

            current = self.root
            while current:
                if value > current.value:
                    if current.right is None:
                        current.right = Node(value)
                        return True
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        current.left = Node(value)
                        return True
                    else:
                        current = current.left
        return False


def is_bin_search_tree(node: Node) -> bool:
    if node is None:
        return True
    is_bst = True
    if node.left is not None:
        if node.value < node.left.value:
            is_bst = False
    if node.right is not None:
        if node.value >= node.right.value:
            is_bst = False
    return is_bin_search_tree(node.left) and is_bst and is_bin_search_tree(node.right)


class TestBinaryTreeUtilities(unittest.TestCase):
    is_bin_search_tree_testcases = [
        ([3, 1, 2], True)
    ]

    def test_is_bst(self):
        tree = Tree()
        tree.add(values=self.is_bin_search_tree_testcases[0][0])
        assert(is_bin_search_tree(tree.root) == self.is_bin_search_tree_testcases[0][1])

        non_bst_bt = Node(5)
        non_bst_bt.left = Node(6)
        non_bst_bt.right = Node(1)

        assert(is_bin_search_tree(non_bst_bt) == False)


unittest.main()
