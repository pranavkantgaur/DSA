# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setRowColMapZero(self, is_seed, row, col, matrix):
        # sets elements as zero along entire row and colm
        i = 0
        while(i < row):
            if matrix[i][col] != 0 and is_seed[i][col] == 0:
                matrix[i][col] = 0
            i+=1
        j = 0
        while(j < col):
            if matrix[row][j] != 0 and is_seed[row][j] == 0:
                matrix[row][j] = 0
            j+=1
                    
                
        # also updates the is_seed map if is_seed
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        is_seed = [[] for row in range(n_rows)]
        for row in range(n_rows):
            is_seed[row] = [1 if matrix[row][col] == 0 else 0 for col in range(n_cols)]
        
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0 and is_seed[row][col] == 1:
                    self.setRowColMapZero(is_seed, row, col, matrix)                                        
                else:
                    continue
                    
        
                    
        
                    
                            
        
