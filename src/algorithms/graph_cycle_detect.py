# You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.
# A cycle is a path in the matrix that starts and ends at the same cell and has four or more cells. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.
# Write a function to find if the matrix has a cycle.

class Solution:  
  def bfs(self, row, col, visited, matrix):
    letter = matrix[row][col]     # l:c
    queue = [[row, col, -1, -1]] # current_row, current_col, parent_row, parent_col, [0, 2, -1, -1]
    while(len(queue)): # q: [[2, 2, 1, 2], [1, 1, 1, 2], [0, 4, 0, 3]]
      level_size = len(queue) # l:3
      for _ in range(level_size): #  2 iter
        row, col, parent_row, parent_col = queue.pop(0)  # r = 1, c=1, p_r=1, p_c=2, # q: [[0, 4, 0, 3], [2, 1, 2, 2]] 
        visited[row][col] = True
        # check neighbors
        if row > 0 and [row - 1, col] != [parent_row, parent_col] and matrix[row - 1][col] == letter: # top
          if visited[row - 1][col] == False: 
            queue.append([row - 1, col, row, col])
            visited[row - 1][col] = True
          else:
            return True
        if row < len(matrix) - 1 and [row + 1, col] != [parent_row, parent_col] and matrix[row + 1][col] == letter: # bottom
          if visited[row + 1][col] == False: 
            queue.append([row + 1, col, row, col]) 
            visited[row + 1][col] = True
          else:
            return True
        if col > 0 and [row, col - 1] != [parent_row, parent_col] and matrix[row][col - 1] == letter: # left
          if visited[row][col - 1] == False: 
            queue.append([row, col - 1, row, col]) 
            visited[row][col - 1] = True
          else:
            return True
        if col < len(matrix[0]) - 1 and [row, col + 1] != [parent_row, parent_col] and matrix[row][col + 1] == letter: # right
          if visited[row][col + 1] == False: 
            queue.append([row, col + 1, row, col]) 
            visited[row][col + 1] = True
          else:
            return True                 
    return False       

  def hasCycle(self, matrix):
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    print(visited)
    for row in range(len(matrix)):
      for col in range(len(matrix[0])):
        if visited[row][col] == False and self.bfs(row, col, visited, matrix):
          return True
    return False
