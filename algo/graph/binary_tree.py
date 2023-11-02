class Node:
    def __init__(self, value):
        self.value = value
        self.right_edge = None
        self.left_edge = None
        # self.length = 1


class BinaryTree:
    def __init__(self, value):
        new_node = Node(value)
        self.ancestor = None
        self.root = new_node

    def append(self, value, node):
        new_node = Node(value)

        if value <= node.value and node.left_edge is None:
            node.left_edge = new_node
        elif value > node.value and node.right_edge is None:
            node.right_edge = new_node

        elif value <= node.value and node.left_edge is not None:
            self.append(value, node.left_edge)
        elif value > node.value and node.right_edge is not None:
            self.append(value, node.right_edge)


binary_tree = BinaryTree(2)
binary_tree.append(3, binary_tree.root)
binary_tree.append(4, binary_tree.root)
binary_tree.append(5, binary_tree.root)
binary_tree.append(2, binary_tree.root)
binary_tree.append(3, binary_tree.root)
binary_tree.append(3, binary_tree.root)
binary_tree.append(4, binary_tree.root)
print(binary_tree)
