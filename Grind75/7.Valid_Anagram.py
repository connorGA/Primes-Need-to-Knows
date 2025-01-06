# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    
# Big O Notation:
    # Time: O(n) - where n is the length of the longest string
    # Space: O(n) - where n is the length of the longest string

def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        
        counter = {}

        for c in s:
            counter[c] = counter.get(c,0) + 1
        
        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1
        
        return all(value == 0 for value in counter.values())

# Big O Notation:
    # Time: O(n) - where n is the length of the lenght of the strings
    # Space: O(k) - where n is the number of unique characters in the string
    