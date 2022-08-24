# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setRowColZero(self, row, col, matrix):
        # sets elements as zero along entire row and colm
        i = 0
        while(i < len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = 0
            i+=1
        j = 0
        while(j < len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = 0
            j+=1
                    
                
        # also updates the is_seed map if is_seed
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])        
        
        # row major
        is_seed_row = [0 for row in range(n_rows)]
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0:
                    is_seed_row[row] = 1
                    break
                else:
                    continue
        # col major
        is_seed_col = [0 for col in range(n_cols)]
        for col in range(n_cols):
            for row in range(n_rows):
                if matrix[row][col] == 0:
                    is_seed_col[col] = 1
                    break
                else:
                    continue            
        for row in range(n_rows):
            for col in range(n_cols):
                if is_seed_row[row] == 1 and is_seed_col[col] == 1:
                    self.setRowColZero(row, col, matrix)                                        
                else:
                    continue
                    
                            
                            
        
                    
        
                    
                            
        
