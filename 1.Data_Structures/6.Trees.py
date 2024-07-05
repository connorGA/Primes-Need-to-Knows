# Trees:
    # A tree is a hierarchical data structure consisting of nodes, with a single node called the root, and sub-nodes called children

# Operations:
    # Insert: Adds a node to the tree
    # Search: Finds a node in the tree
    # Delete: Removes a node from the tree
    # Traversal: Visits all the nodes in a specific order(e.g., in-order, pre-order, post-order)
    # Height: Measures the length of the longest path from the root to a leaf
    # Depth: Measures the distance from the root to a given node
    # Size: Returns the number of nodes in the tree

# Types of Trees:
    # Binary Tree: Each node has at most two children
    # Binary Search Tree(BST): A binary tree where the left child of a node contains values less than the node, and the right child contains values greater than the node
    # AVL Tree: A self-balancing binary search tree where the difference between the heights of left and right subtrees is at most 1
    # Red-Black Tree: A self-balancing binary search tree where nodes follow specific rules to ensure the tree remains balanced
    # B-Tree: A self-balancing search tree in which nodes can have multiple children
    # Trie: A tree used for storing a dynamic set or associative array where keys are usually strings

# Applications:
    # Binary Search Tress(BST): Efficiently supports search, insert, and delete operations
    # Heaps: Implemented as binary trees and used in priority queues
    # Syntax Tress: Used in compilers to represent the structure of program code
    # Tries: Used for efficient information retrieval, such as autocomplete and spell-check features

# Complexity Analysis:
    # Insert: O(log n) for balanced trees, O(n) for unbalanced trees
    # Search: O(log n) for balanced trees, O(n) for unbalanced trees
    # Delete: O(log n) for balanced trees, O(n) for unbalanced trees
    # Traversal: O(n)

# Example of Binary Search Tree(BST) Implementation in Python
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
    
# Example Usage
root = TreeNode(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

# Print in-order traversal of the BST
inorder_traversal(root)  # Output: 20 30 40 50 60 70 80

# PRACTICE PROBLEMS:
# Given a binary tree, determine if it is a valid binary search tree (BST)

def isValidBST(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True
    if not (left < root.val < right):
        return False
    return (isValidBST(root.left, left, root.val) and isValidBST(root.right, root.val, right))

# Example Usage
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isValidBST(root))  # Output: True

# Given a binary search tree(BST), find the lowest common ancestor(LCA) of two given nodes

def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root

# Example Usage
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
p = root.left  # Node with value 2
q = root.right  # Node with value 8
print(lowestCommonAncestor(root, p, q).val)  # Output: 6   
