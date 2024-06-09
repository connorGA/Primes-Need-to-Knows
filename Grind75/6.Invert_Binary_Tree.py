# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:
#                   (4)                         (4)
#                  /   \                       /   \   
#                (2)    (7)     --->         (7)   (2) 
#               /  \    /  \                /  \   /  \
#             (1)  (3)(6)  (9)            (9) (6) (3) (1)

# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]


# Example 2:
#                   (2)                         (2)
#                  /   \          --->         /   \   
#                (1)    (3)                  (3)   (1) 

# Input: root = [2,1,3]
# Output: [2,3,1]


# Example 3:

# Input: root = []
# Output: []


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
#  Big O Notation:
    # Time: O(n) - where n is the number of nodes in the binary tree
    # Space: O(n) - where n is the number of nodes in the binary tree. This space complexity is due to the recursive calls made during the traversal of the tree. 
