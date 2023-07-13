class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.node.value) if self.node else ""

class BinaryTree:

    def __init__(self):
        self._root = None

    def add(self, value):
        if self._root is None:
            self._root = Node(value)
            return
        curr = self._root

        while curr:
            if value > curr.value:
                if curr.right is None:
                    curr.right = Node(value)
                    return
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = Node(value)
                    return
                curr = curr.left

    def preorder(self, node):
        if not node:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def min_height(self, node):
        """
               1
              / \
             2   3
            / \   \
           4   5   6

        The call stack for the find_min_height function could look like this:

        Initial call: find_min_height(node=1)
        Recursive call for the left subtree: find_min_height(node=2)
        Recursive call for the left subtree of node 2: find_min_height(node=4)
        Return from the left subtree of node 4: left_height = 0
        Recursive call for the right subtree of node 2: find_min_height(node=5)
        Return from the right subtree of node 5: right_height = 0
        Return from the left subtree of node 2: left_height = min(0, 0) + 1 = 1
        Recursive call for the right subtree: find_min_height(node=3)
        Recursive call for the right subtree of node 3: find_min_height(node=6)
        Return from the right subtree of node 6: right_height = 0
        Return from the right subtree of node 3: right_height = min(0, 0) + 1 = 1
        Return from the initial call: min(1, 1) + 1 = 2
        In this corrected example, the minimum height of the binary tree is 2.

        """
        if not node:
            return 0

        left_height = self.min_height(node.left)
        right_height = self.min_height(node.right)

        # Return the minimum height of the left and right subtrees, plus 1 for the current level
        return min(left_height, right_height) + 1

    def breadth_first_search(self, value):
        curr_nodes = [self.root]
        while curr_nodes:
            curr = curr_nodes.pop(0)
            if curr.value == value:
                return True
        return False

    def depth_first_search(self):
        pass


tree = BinaryTree()
tree.add(2)
tree.add(1)
tree.add(3)
print(tree.preorder(tree._root))
print("Min depth: " + str(tree.min_height(tree._root)))

tree = BinaryTree()
print(tree.preorder(tree._root))

print(tree.breadth_first_search(3))
print(tree.breadth_first_search(7))
