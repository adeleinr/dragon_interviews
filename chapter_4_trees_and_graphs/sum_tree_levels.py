import unittest

from tree import BinarySearchTree, Node


def sum_levels(root: Node) -> list:
    if root is None:
        return []
    level = 0
    sum_by_levels = []
    curr_nodes = [root]

    while True:
        curr_sum = 0
        queued_nodes = []
        while curr_nodes:
            node = curr_nodes.pop(0)
            curr_sum += node.value
            if node.right:
                queued_nodes.append(node.right)
            if node.left:
                queued_nodes.append(node.left)
        sum_by_levels.append(curr_sum)
        if not queued_nodes:
            return sum_by_levels
        curr_nodes = queued_nodes
        level += 1


class TestBinarySearchTree(unittest.TestCase):
    def test_sunnyday(self):
        tree = BinarySearchTree()
        tree.add(6)
        tree.add(1)
        tree.add(8)
        tree.add(7)
        tree.add(10)

        sum_by_levels = sum_levels(tree.root)
        assert(sum_by_levels == [6, 9, 17])

        tree = BinarySearchTree()
        tree.add(1)
        tree.add(2)
        tree.add(3)
        tree.add(4)
        tree.add(5)
        sum_by_levels = sum_levels(tree.root)
        assert(sum_by_levels == [1, 2, 3, 4, 5])

unittest.main()

