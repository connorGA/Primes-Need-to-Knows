# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

        # (1) -> (2) -> (3) -> (4) -> (5)
        #               |
        #               v
        # (5) -> (4) -> (3) -> (2) -> (1)

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:

        # (1) -> (2)
        #      |
        #      v
        # (2) -> (1)

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Big O Notation:
    # Time: O(n) - where n is the number of nodes in the linked list
    # Space: O(1) - since the variables prev, curr, and nxt are the only extra space used, regardless of the size of the list