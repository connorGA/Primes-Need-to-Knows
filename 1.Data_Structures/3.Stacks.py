# A stack is a linear data structure that follows the "last in first out"(LIFO) principle. This means, the last element added to the stack is the first one to be removed. Stacks are used in various applications, like function call management, expression evalutaion, and back tracking algorthims.

# Basic Operations
    # Push: Add an element to the top of the stack
    # Pop: remove the top element from the stack
    # Peek/Top: retrieve the top element of the stack without removing it
    # isEmpty: check if the stack is empty


# Implementation
    # In Python, a stack can easily be implemented using lists with the 'append()' and 'pop()' methods

# Example Implementation 
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display() # Output: [10, 20, 30]
print(stack.pop()) # Output: 30
print(stack.peek()) # Output: 20
print(stack.is_empty()) # Output: False
stack.display() # Output: [10, 20]


# Use Cases for Stacks:
    # Function Call Management: Stacks are used to manage function calls and recursion. Each time a function is called, a new frame is pushed onto the stack, and when the function returns, the frame is popped off.
    # Expression Evaluation: Stacks are used to evaluate arithmetic expressions, especially those written in postfix notation(Reverse Polish Notation).
    # Backtracking Algorithms: Stacks are used in algorithms that involve backtracking, such as solving mazes, puzzles, and pathfinding problems
    # Undo Mechanisms: Stacks are used to implement undo functionality in applications, where each action is pushed onto a stack and can be popped off to revert the action

# Practice Problems:
# 1. Balanced Parentheses: Write a function to check if a given expression has balanced parentheses
def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ")" and top !="(") or (char  == "}" and top !="{") or (char == "]" and top !="["):
                return False
    return stack.is_empty()

# Test cases
print(is_balanced("()"))  # Output: True
print(is_balanced("({[()]})"))  # Output: True
print(is_balanced("({[)]}"))  # Output: False

# 2. Reverse a String: Write a function to reverse a string using a stack
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    reversed_s = ""
    while not stack.is_empty():
        reversed_s += stack.pop()
    return reversed_s

# Test case
print(reverse_string("hello"))  # Output: "olleh"

# 3. Next Greater Element: Given an array, find the next greater element for each element in the array
def next_greater_element(arr):
    stack = Stack()
    result = [-1] * len(arr)
    for i in range(len(arr) -1, -1, -1):            # Loop through the array in reverse order
        while not stack.is_empty() and stack.peek() <= arr[i]: 
            stack.pop()
        if not stack.is_empty(): 
            result[i] = stack.peek()
        stack.push(arr[i])
    return result

# Test Case
print(next_greater_element([4, 5, 2, 25]))  # Output: [5, 25, 25, -1]
 
