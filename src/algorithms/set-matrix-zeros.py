# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        marked_zero = [[] for row in range(n_rows)]
        for row in range(n_rows):
            marked_zero[row] = [1 for col in range(n_cols)]
        
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0:
                    self.mark_row_col_zero(marked_zero, row, col)                    
                else:
                    continue
                            
        for row in range(n_rows):
            for col in range(n_cols):
                if marked_zero[row][col]:
                    matrix[row][col] = 0
                    
        
                    
                            
        
