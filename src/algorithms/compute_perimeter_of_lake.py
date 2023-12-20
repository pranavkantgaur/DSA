# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1..

# The given matrix has only one island, write a function to find the perimeter of that island.

class Solution:
  
  def dfs(self, row, col, matrix, param_length):
    matrix[row][col] = 2
    # check neighborhood and update param_length
    if row == len(matrix) - 1 or matrix[row + 1][col] == 0: # bottommost
      param_length += 1
    else:
      if matrix[row + 1][col] == 1:
        param_length = self.dfs(row + 1, col, matrix, param_length)        
    if col == len(matrix[0]) - 1 or matrix[row][col + 1] == 0: # rightmost
      param_length += 1
    else:
      if matrix[row][col + 1] == 1:
        param_length = self.dfs(row, col + 1, matrix, param_length)      
    if col == 0 or matrix[row][col - 1] == 0: # left most
      param_length += 1      
    else:
      if matrix[row][col - 1] == 1:
        param_length = self.dfs(row, col - 1, matrix, param_length)   
    if row == 0 or matrix[row - 1][col] == 0: # topmost
      param_length += 1
    else:
      if matrix[row - 1][col] == 1: 
        param_length = self.dfs(row - 1, col, matrix, param_length)   
    return param_length
  
  def findIslandPerimeter(self, matrix):
    param_length = 0
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if matrix[row][col]:
          param_length = self.dfs(row, col, matrix, param_length)
          return param_length
    return param_length
