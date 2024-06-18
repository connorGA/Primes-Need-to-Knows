# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 
# Example 1:
#                   (6)
#                  /   \
#                (2)   (8)
#               /   \ /   \
#             (0) (4)(7)  (9)
#                /  \
#              (3)   (5)

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.

# Example 2:
#                   (6)
#                  /   \
#                (2)   (8)
#               /   \ /   \
#             (0) (4)(7)  (9)
#                /  \
#              (3)   (5)

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

# IMPORTANT TO REMEMBER: Binary tree ordered according to .val, where greater node is branched to the right and lesser node is branched left.


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
# Big O Notation:
    # Time: O(log n) - where n is the heigh of the tree
    # Space: O(1) - we arent using any data structs to store values, just keeping track of variables and updating curr node