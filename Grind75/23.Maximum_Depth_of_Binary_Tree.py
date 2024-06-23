# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
#               (3)
#              /   \
#            (9)    (20)
#                  /    \
#                (15)    (7)


# Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2

# THREE WAYS TO SOLVE -------

# FIRST - RECURSION:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Big O Notation:
    # Time: O(n) - where n is the number of nodes in the binary tree
    # Space: O(h) - where h is the height of the binary tree
    

# SECOND - ITERATIVE DFS:
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        stack = [[root, 1]]
        res = 1

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
# Big O Notation:
    # Time: O(n) - where n is the number of nodes in the binary tree
    # Space: O(h) - where h is the height of the binary tree


# THIRD - BFS:
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        level = 0
        q = deque([root])
        while q:

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level += 1
        return level

# Big O Notation:
    # Time: O(n) - where n is the number of nodes in the binary tree
    # Space: O(m) - where m is the maximum number of nodes at any level in the binary tree


        