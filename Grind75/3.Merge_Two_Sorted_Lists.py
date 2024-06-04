# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

        # Input: (1) --> (2) --> (4)            (1) --> (3) --> (4)
        # Output:     (1) --> (1) --> (2) --> (3) --> (4) --> (4)

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:

# Input: list1 = [], list2 = []
# Output: []
 
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

# Big O Notation:
    # Time: O(n + m) - where n is the lenght of l1 and m is the lenght of l2
    # Space: O(1) - As the function uses a constant amount of extra space