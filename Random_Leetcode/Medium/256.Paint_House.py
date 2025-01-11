# There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.
# For example, costs[0][0] is the cost of painting house 0 with the color red; costs[1][2] is the cost of painting house 1 with color green, and so on...
# Return the minimum cost to paint all houses.

 
# Example 1:
# Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
# Minimum cost: 2 + 5 + 3 = 10.

# Example 2:
# Input: costs = [[7,6,2]]
# Output: 2

class Solution(object):                     ##### WRONG SOLUTION - DOESNT ACCOUNT FOR ADJACENT HOUSE CONSTRAINT
    def minCost(self, costs):
        minPrice = 0
        for row in costs:
            min = 0 
            for i in row:
                if min == 0 or i < min:
                    min = i
            minPrice += min
            
        return minPrice

# Big O Notation:
    # Time: O(m x n) - the method needs run through every array in every row
    # Space: O(1) - minPrice and min are scalar variables, no additional space is required
                


# CORRECT SOLUTION - PASSES ALL TEST CASES
class Solution(object):
    def minCost(self, costs):
        if not costs:
            return 0
        
        # Iterate from the second-to-last house to the first house
        for i in range(len(costs) - 2, -1, -1):
            # Update the current house cost by adding the minimum cost of painting the next house
            costs[i][0] += min(costs[i + 1][1], costs[i + 1][2])  # Red
            costs[i][1] += min(costs[i + 1][0], costs[i + 1][2])  # Blue
            costs[i][2] += min(costs[i + 1][0], costs[i + 1][1])  # Green
        
        # Return the minimum cost of painting the first house
        return min(costs[0][0], costs[0][1], costs[0][2])

# Big O Notation:
    # Time: O(n) - where n is the number of houses
    # Space: O(1) - modifes the costs matrix in place without using additional space