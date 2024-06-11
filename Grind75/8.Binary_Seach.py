# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# MY FIRST TRY SOLUTION O(n) - not in O(log n)
class Solution(object):
    def search(self, nums, target):
        

        for i,num in enumerate(nums):
            if num == target:
                return i
        if target not in nums:
            return -1
        
# Neetcode solution - Proper binary search

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
            
# Big O Notation:
    # Time: O(log n) - where n is the number of elements in the list
    # Space: O(1) - since the algo only uses a few variables (l, r, m) to keep track of indices, and these variables do not scale with the size of the input list