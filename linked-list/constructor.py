class Node:
    def __init__(self, value):
        self.value = value

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        self.next = None

my_linked_list = LinkedList(4)

# print(my_linked_list.node)
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
