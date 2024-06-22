# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.


# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.

from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        count = defaultdict(int)
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2
        
        for cnt in count.values():
            if cnt % 2 == 1:
                res += 1
                break
        
        return res
    
# Big O Notation:
    # Time: O(n) - where n is the lenght of the input string s
    # Space: O(m) - where m is the number of unique characters in the input string s



