# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# There are no lakes on the island, so the water inside the island is not connected to the water around it. A cell is a square with a side length of 1..

# The given matrix has only one island, write a function to find the perimeter of that island.

class Solution:
  def dfs(self, row, col, matrix, param_length):
    stack = [[row, col]]
    while(len(stack)):
      top_row, top_col = stack.pop()      
      # check neighbors
      if top_row == 0 or matrix[top_row - 1][top_col] == 0:
        param_length += 1
      else:
        if matrix[top_row - 1][top_col] == 1:
          stack.append([top_row - 1, top_col])
          matrix[top_row - 1][top_col] = 2
      if top_row == len(matrix) - 1 or matrix[top_row + 1][top_col] == 0:
        param_length += 1
      else:
        if matrix[top_row + 1][top_col] == 1:
          stack.append([top_row + 1, top_col])        
          matrix[top_row + 1][top_col] = 2
      if top_col == 0 or matrix[top_row][top_col - 1] == 0:
        param_length += 1
      else:
        if matrix[top_row][top_col - 1] == 1:
          stack.append([top_row, top_col - 1])      
          matrix[top_row][top_col - 1] = 2
      if top_col == len(matrix[0]) - 1 or matrix[top_row][top_col + 1] == 0:
        param_length += 1
      else:
        if matrix[top_row][top_col + 1] == 1:
          stack.append([top_row, top_col + 1])        
          matrix[top_row][top_col + 1] = 2
    return param_length
  
  def findIslandPerimeter(self, matrix):
    param_length = 0
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if matrix[row][col]:
          matrix[row][col] = 2
          param_length = self.dfs(row, col, matrix, param_length)
          return param_length
    return param_length
