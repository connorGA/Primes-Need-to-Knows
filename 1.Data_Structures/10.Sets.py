# Sets:
    # A set is a data structure that stores unique elements(NO DUPLICATES) and supports various operations like addition, deletion, and membership testing

# Operations: 
    # Add: adds an element to the set
    # Remove: Removes an element from the set
    # Contains: Checks if an element is in the set
    # Union: Combines elements from two sets
    # Intersection: Finds common elements between two sets
    # Difference: Finds elements present in one set but not in another
    # Subset: Checks if one set is a subset of another

# Applications:
    # Removing Duplicates: Used to remove duplicates from a collection
    # Membership Testing: Efficiently check if an element exists in a collection
    # Set Operations: Used in problems involving union, intersection, and difference of sets
    # Graph Algorithms: Used to represent and manipulate sets of vertices or edges

# Complexity of Analysis:
    # Add: O(1) on average
    # Remove: O(1) on average
    # Contains: O(1) on average
    # Union: O(n) where n is the total number of elements
    # Intersection: O(min(len(set1), len(set2)))
    # Difference: O(len(set1))

# Creating a set
my_set = set()

# Adding elements
my_set.add(1)
my_set.add(2)
my_set.add(3)

# Removing elements
my_set.remove(2)

# Checking membership
print(1 in my_set)  # Output: True
print(2 in my_set)  # Output: False

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Subset
print({1, 2}.issubset(set1))  # Output: True
print({1, 4}.issubset(set1))  # Output: False


# PRACTICE PROBLEMS:
# Given two arrays, write a function to compute their intersection
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list(set1.intersection(set2))

# Example Usage
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))  # Output: [2]

# Given a non-empty array of integers where every element appears twice except for one, find that single one
def singleNumber(nums):
    return 2 * sum(set(nums)) - sum(nums)

# Example Usage
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
