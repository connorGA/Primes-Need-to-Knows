# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with color.
# Return the modified image after performing the flood fill.

from collections import deque 
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        if not image:
            return image
        
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]

        if originalColor == color:
            return image
        
        queue = deque([(sr, sc)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y = queue.popleft()
            image[x][y] = color

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if  0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == originalColor:
                    queue.append((nx, ny))
                    image[nx][ny] = color
        return image

# Big O Notation:
    # Time: O(n) where n is the total number of pixels in the image.
    # Space: O(n) where n is the total number of pixels in the image, this is because the queue can potentially hold up to all the pixels in the worst case.