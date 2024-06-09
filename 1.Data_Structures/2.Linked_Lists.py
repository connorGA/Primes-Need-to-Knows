# Linked lists store a sequence of elements. Unlike arrays, linked lists are not stored in contiguous memory locations, which allows for efficient insertion and deletion operations.

# Types of Linked Lists:
    # Singly Linked List: Each node points to the next node in the sequence
    # Doubly Linked List: Each node points to both the next and the previous node
    # Circular Linked List: The last node points back to the first node, forming a circle.

# Singly Linked List
    # Structure: A singly linked list is a collection of nodes where each node contains:
            # Data: The value stored in the node
            # Next: A reference (or pointer) to the next node in the list
    # Basic Operations:
            # Traversal: Visiting each node in the list
            # Insertion: Adding a new node to the list
            # Deletion: Removing a node from the list
            # Search: Finding a node in the list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

# Create a new linked list
ll = SinglyLinkedList()

# Insert elements
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)

# Insert at beginning
ll.insert_at_beginning(0)

# Traverse and print the list
ll.traverse()  # Output: 0 -> 1 -> 2 -> 3 -> None

# Search for an element
print(ll.search(2))  # Output: True
print(ll.search(5))  # Output: False

# Delete an element
ll.delete_node(2)
ll.traverse()  # Output: 0 -> 1 -> 3 -> None