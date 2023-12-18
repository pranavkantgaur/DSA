# Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color. The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell. Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

# Given a matrix, a starting cell, and a color, flood fill the matrix.
class Solution:
  def dfs(self, row_s, col_s, cell_value_s, color, matrix):
    matrix[row_s][col_s] = color
    if row_s + 1 < len(matrix) and matrix[row_s + 1][col_s] == cell_value_s:
        self.dfs(row_s + 1, col_s, cell_value_s, color, matrix)
    if col_s - 1 >= 0 and matrix[row_s][col_s - 1] == cell_value_s:
        self.dfs(row_s, col_s - 1, cell_value_s, color, matrix)
    if col_s + 1 < len(matrix[0]) and matrix[row_s][col_s + 1] == cell_value_s:
        self.dfs(row_s, col_s + 1, cell_value_s, color, matrix)
    if row_s - 1 >= 0 and matrix[row_s - 1][col_s] == cell_value_s:
      self.dfs(row_s - 1, col_s, cell_value_s, color, matrix)
    return
  
  def floodFill(self, matrix, x, y, newColor):
      if  0 > x >= len(matrix) or 0 > y >= len(matrix[0]): 
        return matrix
      self.dfs(x, y, matrix[x][y], newColor, matrix)
      return matrix
