class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def print_values(self):
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

    def prepend(self, value):
        new_node = Node(value)
        pointer_old_head = self.head
        new_node.next = pointer_old_head
        self.head = new_node
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

    def pop_first(self):
        pointer_next_head = self.head.next
        self.head = pointer_next_head
        self.length -= 1
        return True

    def find_middle(self):
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

    def has_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def get_node_by_index(self, index):
        if self.length < index < 0:
            return None

        temp_pointer = self.head
        for _ in range(index):
            temp_pointer = temp_pointer.next
        return temp_pointer

    def reverse(self):
        current_node = self.head
        self.head = self.tail
        self.tail = current_node
        previous_node = None

    def remove(self, index):
        if self.length < index < 0:
            return None


my_ll = LinkedList(4)
my_ll.append(5)
my_ll.append(7)
my_ll.append(8)

# testing the functions

# my_ll.print_values()
# print(my_ll.find_middle().value)
# my_ll.has_loop()
# print(my_ll.get_node_by_index(2).value)  # don't forget the index starts with 0

# my_ll.pop()
# my_ll.prepend(10)
# my_ll.pop_first()
# my_ll.print_values()

my_ll.reverse()
# my_ll.print_values()

# my_ll.remove()
my_ll.print_values()
