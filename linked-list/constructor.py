class Node:
    def __init__(self, value):
        # Node contains:
        self.value = value # Value &
        self.next = None # Pointer

class LinkedList:
    def __init__(self, value):
        # Initialise a linked list with its first node
        new_node = Node(value)
        # LinkedList has:
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_items(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Create new node
        new_node = Node(value)

        # Set the pointer of the previous node to the current value
        self.tail.next = new_node

        # Set the tail to the new node & Increase length
        self.tail = new_node
        self.length += 1

    def pop(self):
        # Remove Item
        self.length -= 1

# Initialise Linked List
my_linked_list = LinkedList(4)

# Append a Node
my_linked_list.append(5)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

# Print Items
my_linked_list.print_items()
