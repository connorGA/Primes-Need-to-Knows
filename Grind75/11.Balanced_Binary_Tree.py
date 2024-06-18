# Given a binary tree, determine if it is hieght-balanced(A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.)

 
# Example 1:
#               (3)
#              /   \ 
#            (9)    (20)
#                   /  \
#                 (15)  (7)

# Input: root = [3,9,20,null,null,15,7]
# Output: true


# Example 2:
#               (1)
#              /   \ 
#            (2)    (2)
#           /  \
#        (3)   (3)
#       /   \
#     (4)   (4)

# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
# Example 3:

# Input: root = []
# Output: true


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def dfs(root):
            if not root: return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# Big O Notation:
    # Time: O(n) where n is the number of nodes in the binary tree. Each node is visisted exactly once, and the operations at each node(calculating heights and checking balance conditions) are O(1)
    # Space: O(h) where h is the height of the binary tree


# Explanation:
    # This method efficiently determines whether a binary tree is balanced leveraging DFS to compute subtree heights and checking balance conditions at each node, ensuring that both time and space complexities are suitable for typical binary tree operations