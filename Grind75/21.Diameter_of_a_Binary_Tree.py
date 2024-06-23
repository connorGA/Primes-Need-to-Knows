# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Example 1:
#               (1)
#              /   \
#            (2)    (3)
#           /   \
#         (4)    (5)
# Input: root = [1,2,3,4,5]
# Output: 3
# Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].


# Example 2:
# Input: root = [1,2]
# Output: 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]                                       # Initialize a list to hold the maximum diameter, this is a global variable 

        def dfs(root):
            if not root:
                return -1                               # Base case: If root is None, return None because for null tree, height is -1
            left = dfs(root.left)                       # Recursively calculate the depths of the left and right subtrees
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)      # Update the maximum diameter found so far

            return 1 + max(left, right)                 # return the depth of the current node
        
        dfs(root)                                       # start DFS traversal from the root node
        return res[0]                                   # Return the maximum diamter found 
        
# Big O Notation:
    # Time: O(n) - where n is the number of nodes in the binary tree
    # Space: O(n) - due to the recursion stack space used during DFS traversal, with O(1) additional space