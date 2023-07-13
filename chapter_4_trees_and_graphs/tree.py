class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def get(self, value):
        # Does a DFS
        assert self._root, "value {} not found".format(value)
        nodes_to_check = [self._root]
        while nodes_to_check:
            node = nodes_to_check.pop()
            if node.value == value:
                return value
            if node.right:
                nodes_to_check.append(node.right)
            if node.left:
                nodes_to_check.append(node.left)
        return None

    def get_recursive(self, value):
        assert self._root, "value {} not found".format(value)
        return self.get_helper(value, self._root)

    def get_helper(self, value, node):
        if node.value == value:
            return value
        if node.right:
            self.get_helper(value, node.right)
        if node.left:
            self.get_helper(value, node.left)
        return None

    def add(self, value):
        if self._root is None:
            self._root = Node(value)
            return self._root

        current = self._root
        while current:
            if value >= current.value:
                # Find a right leave
                if not current.right:
                    current.right = Node(value)
                    return
                 # otherwise keep moving to the right
                current = current.right
            else:
                # or find a left leave
                if not current.left:
                    current.left = Node(value)
                    return
                # otherwise keep moving to the left
                current = current.left

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.value] + self.inorder(node.right)

    def preorder(self, node):
        if node is None:
            return []
        return [node.value] + self.preorder(node.left) + self.preorder(node.right)

    def breadth_first_search(self, value):
        curr_nodes = [self._root]
        while curr_nodes:
            curr = curr_nodes.pop(0)
            if curr.value == value:
                return True
            if curr.right:
                curr_nodes.append(curr.left)
            if curr.left:
                curr_nodes.append(curr.right)
        return False

    def depth_first_search(self, value):
        return self.depth_first_search_helper(self._root, value)

    def depth_first_search_helper(self, node, value):
        if not value or not node:
            return
        if node.value == value:
            return True
        return (
            self.depth_first_search_helper(node.left, value) or
            node.value == value or
            self.depth_first_search_helper(node.right, value)
        )

tree = BinarySearchTree()
tree.add(2)
tree.add(1)
tree.add(3)

print(tree.breadth_first_search(3))
print(tree.breadth_first_search(7))

print(tree.depth_first_search(3))
