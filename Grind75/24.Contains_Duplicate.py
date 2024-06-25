# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# My solution - Hashmap with loop over nums array
class Solution(object):
    def containsDuplicate(self, nums):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
                return True
            else:
                count[num] = 1
                
        return 

# Big O Notation:
    # Time: O(n) - where n is the lenght of the nums array
    # Space: O(n) - where n is the length of the nums array since worst case, we add all values to hashmap
    


        