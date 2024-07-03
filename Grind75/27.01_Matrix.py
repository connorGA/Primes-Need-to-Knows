# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.

# Example 1:
#   (0)(0)(0)
#   (0)(1)(0)
#   (0)(0)(0)
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
#   (0)(0)(0)
#   (0)(1)(0)
#   (1)(1)(1)
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        distance = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # Enqueue all 0 cells
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                    distance[r][c] = 0

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Perform BFS
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and distance[nr][nc] == float('inf'):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        return distance

# Big O Notation:
    # Time: O(m x n) - where m is the number of rows and n is the number of columns in the matrix
    # Space: O(m x n) - in the worst case, the queue can hold all the cells in the matrix