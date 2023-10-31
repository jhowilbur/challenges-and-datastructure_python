class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_value(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        pre_node = self.head
        selected_node = self.head

        while selected_node.next:
            pre_node = selected_node
            selected_node = selected_node.next
        self.tail = pre_node
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return pre_node

    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer


my_ll = LinkedList(4)
my_ll.append(5)
my_ll.append(7)
my_ll.append(8)
# my_ll.print_value()

print(my_ll.find_middle().value)