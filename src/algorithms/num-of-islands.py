class Solution:
  def dfs(self, row, col, matrix):
    matrix[row][col] = 0
    if row + 1 < len(matrix) and matrix[row+1][col]: self.dfs(row+1, col, matrix)
    if col + 1 < len(matrix[0]) and matrix[row][col + 1]: self.dfs(row, col+1, matrix)
    if col - 1 >= 0 and matrix[row][col-1]: self.dfs(row, col - 1, matrix)
    return
  def countIslands(self, matrix):
    totalIslands = 0
    for row in range(len(matrix)):
      for col in  range(len(matrix[0])):
        if matrix[row][col]:
          totalIslands += 1
          self.dfs(row, col, matrix)
    return totalIslands
