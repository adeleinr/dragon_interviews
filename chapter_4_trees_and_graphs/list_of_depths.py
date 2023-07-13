import unittest


class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return self.value + " right: " + self.right.value + " left: " + self.left.value

class LinkListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value + " next: " + self.next.value


class BinTree:

    def __init__(self):
        self.root = None

    def build_tree(self, lst):
        for value in lst:
            self.add(value)

    def add(self, value):
        if self.root is None:
            self.root = BinTreeNode(value)
            return self.root

        current = self.root
        while current:
            if value < current.value:
                if current.left is None:
                    current.left = BinTreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BinTreeNode(value)
                    return
                current = current.right

        return self.root

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    """
    Given a binary tree, design an algorithm which creates a linked
    list of all the nodes at each depth (e.g., if you have a tree with
    depth D, you'll have D linked lists).
    """
    def build_depth_list(self):
        linked_lists = []
        linked_list_level = 0
        nodes_at_current_level = [self.root]

        while True:
            children = []
            prev = None

            while nodes_at_current_level:
                curr = nodes_at_current_level.pop(0)
                new_node = LinkListNode(curr.value)

                if prev is None:
                    linked_lists.append(new_node)
                    prev = new_node
                else:
                    prev.next = new_node
                    prev = new_node
                if curr.left is not None:
                    children.append(curr.left)
                if curr.right is not None:
                    children.append(curr.right)
            if children:
                nodes_at_current_level = children
                linked_list_level += 1
                prev = None
            else:
                break
        return linked_lists

    def format(self, lst):
        print_result = []
        for node in lst:
            level_str = ""
            while node:
                level_str += node.value + " "
                node = node.next
            print_result.append(level_str)
        return print_result


class TestLinkedListByLevel(unittest.TestCase):

    testcases = [
        (["D", "B", "A", "C", "G", "F", "H"], ["D", "B G", "A C F H"])
    ]

    def test_build_by_depth(self):
        tree = BinTree()
        tree.build_tree(self.testcases[0][0])
        print(tree.inorder(tree.root))
        print(tree.format(tree.build_depth_list()))


unittest.main()