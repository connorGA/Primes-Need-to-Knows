# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# NOTE: When adding binary, 1 + 1 results in O plus a carry one. Imagine it like this:
# 
#                       11             (binary '1, 1' not int '11')
#                     +  1             1+1= 0, then carry the one, so again 1+1 is 0, carry another 1, since the one is alone it is just 1, thus 100
#                      ---- 
#                      100

class Solution(object):
    def addBinary(self, a, b):
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            res = char + res
            carry = total // 2

        if carry:
            res = "1" + res
        return res

# Big O Notation:
    # Time: O(max(len(a), len(b)))
    # Space: O(max(len(a), len(b)))

# This function efficiently computes the sum of two binary strings 'a' and 'b' by iterating through them in reverse order, handling carries, and constructing the resulting binary string in reverse.
# The complexities ensure that it operates in linear time relative to the length of the longer input string and uses linear additional space for the output string 'res'