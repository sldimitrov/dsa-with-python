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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Set the pointer of the previous node to the current value
            self.tail = new_node
        self.length += 1
        return True

    def preprend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length is None:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        pre.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        next_node = self.tail
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp.value


# Initialise Linked List
my_linked_list = LinkedList(4)

# Append a Node
my_linked_list.append(5)
my_linked_list.append(5)

print("Print items before pop")
my_linked_list.print_items()

my_linked_list.pop()

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

# Print Items
print("Print items after pop")

my_linked_list.preprend(3)
print(my_linked_list.pop_first())

my_linked_list.print_items()

