# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# A closed island is an island that is totally surrounded by 0s (i.e., water). This means all horizontally and vertically connected cells of a closed island are water. This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

# Write a function to find the number of closed islands in the given matrix.

class Solution:
  def dfs(self, x, y, matrix):
    matrix[x][y] = 0    
    is_closed = True
    if x <= 0 or x >= len(matrix) - 1 or y <= 0 or y >= len(matrix[0]) - 1:
        is_closed = False
    if y + 1 < len(matrix[0]) and matrix[x][y + 1]:
       is_closed &= self.dfs(x, y + 1, matrix) 
    if x + 1 <= len(matrix) and matrix[x + 1][y]:
        is_closed &= self.dfs(x + 1, y, matrix) 
    if y - 1 >= 0 and matrix[x][y - 1]: 
        is_closed &= self.dfs(x, y - 1, matrix)
    return is_closed

  
  def countClosedIslands(self, matrix):
    n_closed_islands = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] and self.dfs(row, col, matrix): 
              n_closed_islands += 1
    return n_closed_islands
