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
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

# Big O Notation
    # Time: O(n) - because we only have to go through every input character once
    # Space: O(n) - we're using a stack, which can be up to the size of the input in worst case