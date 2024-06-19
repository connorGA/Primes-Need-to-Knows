# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
    # void push(int x) Pushes element x to the back of the queue.
    # int pop() Removes the element from the front of the queue and returns it.
    # int peek() Returns the element at the front of the queue.
    # boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
    # You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    # Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
    

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]

# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false

class MyQueue(object):

    def __init__(self):                                 # Time: O(1) - initializing two empty lists has a constant time complexity
        self.s1 = []                                    # Space: O(1) - the space used is constant, as it only involves creating two empty lists
        self.s2 = []
        

    def push(self, x):                                  # Time: O(1) - appending an element to a list('s1') has constant time complexity
        self.s1.append(x)                               # Space: O(1) - adding an element to a list('s1') doesnt increase the input size beyond the single element added
        

    def pop(self):                                      # Time: Amortized O(1) - The pop operation involves moving all elements from 's1' to 's2' only when 's2' is empty, which is an amortized constant time operation due to Pythons list operations. Once 's2' has elements, popping from it is O(1) 
        if not self.s2:                                 # Space: O(n) - In the worst case, if all elements are in 's1', 's2' will contain all elements after the 'pop' operation completes, resulting in O(n) space complexity
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        

    def peek(self):                                     # Time: Amortized O(1) - Similar to pop, moving elements to 's2' happens only when 's2' is empty, making the operation amortized O(1). Accessing the element in 's2' is also O(1)
        if not self.s2:                                 # Space: O(n) - Similar to pop, in the worst case where all elements are in 's1', 's2' will hold all elements temporarily, resulting in O(n) space complexity
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self):                                    # Time: O(1) - Checking the lenght of both 's1' and 's2' and comparing them is constant time
        return max(len(self.s1), len(self.s2)) == 0     # Space: O(1) - only a constant amount of space is used to store the lengths of 's1' and 's2'
        


