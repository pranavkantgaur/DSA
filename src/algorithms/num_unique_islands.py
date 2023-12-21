# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water). Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

# Write a function to find the number of distinct islands in the given matrix.
class Solution: 
  def dfs(self, row, col, matrix, current_path_str, path_strings):
    stack = [[row, col, '']]
    while(len(stack)):    
        row, col, direct = stack.pop()
        current_path_str += direct        
        matrix[row][col] = 0
        if matrix[row][col-1]:
            stack.append([row, col - 1, 'l'])
            matrix[row][col - 1] = 0
        if matrix[row][col+1]:
            stack.append([row, col + 1, 'r'])
            matrix[row][col + 1] = 0
        if matrix[row - 1][col]:
            stack.append([row - 1, col, 't'])
            matrix[row - 1][col] = 0
        if matrix[row + 1][col]:
            stack.append([row + 1, col, 'b'])
            matrix[row + 1][col] = 0
    path_strings.add(current_path_str)

  def findDistinctIslandsDFS(self, matrix):
    path_strs = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                current_path_str = ''
                self.dfs(row, col, matrix, current_path_str, path_strs)
    return len(path_strs)

