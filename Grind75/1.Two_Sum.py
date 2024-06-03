# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for i, num in enumerate(nums):
            match = target - num

            if match in prevMap:
                return [prevMap[match], i]
            else:
                prevMap[num] = i

        return
    
#  Big O Notation
    # Time: O(n) - where n is the length of 'nums'. Note: dictionary insertion and lookup operations are average O(1)
    # Space: O(n) - worst case, we might store every element of 'nums' in 'prevMap', thus space required is proportional to the number of elements in 'nums'

