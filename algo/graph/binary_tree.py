from functools import wraps


def default_node(f):  # decorator to avoid all the time use if node is None in the methods
    @wraps(f)
    def wrapper(self, *args, **kwargs):
        if 'node' not in kwargs or kwargs['node'] is None:
            kwargs['node'] = self.root
        return f(self, *args, **kwargs)
    return wrapper


class Node:
    def __init__(self, value):
        self.value = value
        self.right_edge = None
        self.left_edge = None
        # self.length = 1


class BinaryTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node

    @default_node
    def append(self, value, node=None):
        new_node = Node(value)
        side = 'left_edge' if value <= node.value else 'right_edge'
        if getattr(node, side) is None:
            setattr(node, side, new_node)
        else:
            self.append(value, node=getattr(node, side))

    @default_node
    def print_tree(self, node=None):
        print(node.value)
        if node.right_edge:
            self.print_tree(node=node.right_edge)
        if node.left_edge:
            self.print_tree(node=node.left_edge)

    # TODO complete the remove method
    @default_node
    def remove_big_node(self, node=None):
        while node.right_edge is not None:
            actual_node = node
            node = node.right_edge
            if node.right_edge is None:
                actual_node.right_edge = None
                return actual_node


binary_tree = BinaryTree(2)
# binary_tree.append(3)
# binary_tree.append(4)
# binary_tree.append(5)
# binary_tree.append(2)
# binary_tree.append(3)
# binary_tree.append(3)
# binary_tree.append(4)

binary_tree.append(3)
binary_tree.append(4)
binary_tree.append(5)

binary_tree.print_tree()

# binary_tree = binary_tree.remove_big_node()
#
# print(binary_tree)
