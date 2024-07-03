# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution(object):
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        
        # Add all intervals before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            i += 1
        
        # Add the merged interval
        res.append(newInterval)
        
        # Add the remaining intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res

# Example Usage
solution = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(solution.insert(intervals, newInterval))  # Output: [[1, 5], [6, 9]]

# Big O Notation:
    # Time: O(n) - since each interval is processed exactly once across all loops
    # Space: O(n) - because in worst case it stores all the n+1 intervals(the original 'n' intervals plus the newInterval)
