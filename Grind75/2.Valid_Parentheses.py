# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.
    # Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
    # Input: s = "()"
    # Output: true

# Example 2:
    # Input: s = "()[]{}"
    # Output: true

# Example 3:
    # Input: s = "(]"
    # Output: false

class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in closeToOpen:                                    # this works because it is only checking the key char in the dict, aka closing parentheses. If c is a closing parenthesis, we want to make sure our stack isnt empty(that would be invalid) and we want to check if the parenthesis at the top of the stack matches. If its not a closing parenth, we'll just skip that if statement and move to the next where we append it to the stack. 
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False                         # can only return True if stack is empty

# Big O Notation
    # Time: O(n) - because we only have to go through every input character once
    # Space: O(n) - we're using a stack, which can be up to the size of the input in worst case