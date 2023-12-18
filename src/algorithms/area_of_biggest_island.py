# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it. Write a function to return the area of the biggest island. 

An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).
class Solution:
  def dfs(self, row, col, area, matrix):
    matrix[row][col] = 0 # visited
    area += 1
    # visit neighbors
    if row + 1 < len(matrix) and matrix[row + 1][col]: area = self.dfs(row + 1, col, area, matrix)
    if col + 1 < len(matrix[0]) and matrix[row][col + 1]: area = self.dfs(row, col + 1, area, matrix)
    if col - 1 >= 0 and matrix[row][col - 1]: area = self.dfs(row, col - 1, area, matrix)
    return area

  def maxAreaOfIsland(self, matrix):
    biggestIslandArea = 0
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if matrix[row][col]:
          area = 0
          biggestIslandArea = max(self.dfs(row, col, area, matrix), biggestIslandArea)
    return biggestIslandArea
