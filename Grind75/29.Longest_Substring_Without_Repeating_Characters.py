# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# SLIDING WINDOW SOLUTION

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:         # if its already in our charSet(duplicate), we will remove the left most duplicate and update the position of l, thus sliding the window 
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l + 1)       # +1 necessary to give accurate length of current substring, since l and r are keeping track of index
        return res
    
# Big O Notation:
    # Time: O(n) - where n is the number of chars in s
    # Space: O(n) - where n is the number of chars in s