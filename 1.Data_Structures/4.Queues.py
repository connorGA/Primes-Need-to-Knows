# A queue is a linear data structure that follows the First In, First Out(FIFO) principle. In a queue, elements are added at the rear(enqueue) and removed from the front(dequeue). It operates like a real-wolrd queue or line, where the first person to join the queue is the first one to be served.

# Operations:
    # Enqueue: Adds an element to the rear of the queue
    # Dequeue: Removes and returns the element from the front of the queue
    # Front: Returns the element at the front of the queue without removing it
    # IsEmpty: Checks if the queue is empty
    # Size: Returns the number of elements currentrly in the queue

# Implementation:
    # Array-based implementation: In this implementation, a fixed-size array us used to store the elements of the queue. It requires keepeing track of the front end rear pointers to perform enqueue and dequeue operations efficiently. However, reszing the array can be costly if it becomes full.
    # Linked list-based implementation: In this implementation, a linked list is used to store the elements of the queue. It allows for dynamic resizing without the need to copy elements. However, it requires addtional memory for maintaining the links between elements.

# Applications:
    # Breadth-First Search(BFS): Used to traverse graphs level by level, visiting all nodes at the current level before moving to the next level
    # Process Scheduling: Queues are used to manage processes in operating systems, where each process is added to a queue and scheduled for execution based on its priority or arrival time
    # Buffer Management: Queues are used to manage buffers in networking and communication systems to store incoming data packets until they can be processed.

# Complexity Analysis:
    # Enqueue: O(1)
    # Dequeue: O(1)
    # Front: O(1)
    # IsEmpty: O(1)
    # Size: O(1)

Queue = [5, 2, 9, 1, 7]

# Enqueue(4): Front [5,2,9,1,7,4] Rear
# Dequeue: Front [2,9,1,7,4] Rear
# Front: '2'
# IsEmpty: 'False
# Size: '5'


# Problem 1: Implement Stack using Queues
    #  Design a stack that supports push, pop, top, and retrieving the minimum element in constant time
    # Implement the MinStack class:
        # MinStack() initializes the stack object.
        # void push(int val) pushes the element val onto the stack.
        # void pop() removes the element on the top of the stack.
        # int top() gets the top element of the stack.
        # int getMin() retrieves the minimum element in the stack.
    
from collections import deque

class MinStack:
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()
    
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

# Example Usage
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())      # Output: 0
print(min_stack.getMin())  # Output: -2

# Problem 2: Binary Tree Level Order Traversal
    #  Given the root of a binary tree, return the level order traversal of its nodes' values(i.e., from left to right, level by level)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: TreeNode):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Example Usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]