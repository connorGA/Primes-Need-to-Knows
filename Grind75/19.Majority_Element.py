# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


# MY SOLUTION - WORKED FIRST TIME :)
class Solution(object):
    def majorityElement(self, nums):
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        return max(counter)
    
# Big O Notation:
    # Time: O(n) - where n is the length of nums array
    # Space: O(n) - where n is the length of nums array
        

# NEETCODE SOLUTION - Uses "Boyer Moore Algorithm" and has O(1) space
class Solution(object):
    def majorityElement(self, nums):
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res      
    
# Big O Notation:
    # Time: O(n) - where n is the length of nums array
    # Space: O(1) - storing in res and count vars