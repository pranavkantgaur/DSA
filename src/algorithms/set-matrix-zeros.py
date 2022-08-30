# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:                
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])        
        row0 = -1
        col0 = -1
        
        # get status of row0
        for col in range(n_cols):
            if matrix[0][col] == 0:
                row0 = 0
                break
        # get status of col0        
        for row in range(n_rows):
            if matrix[row][0] == 0:
                col0 = 0
                break
        # get status of rows from 1 to n - 1                
        for row in range(1, n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    break
        # get status of cols 1 to n - 1                         
        for col in range(1, n_cols):
            for row in range(n_rows):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    break                        
        # zero out rows 1 to n - 1 depending on status set earlier
        for row in range(1, n_rows):            
            if matrix[row][0] == 0:
                for col in range(1 , n_cols):
                    matrix[row][col] = 0
        # zero out cols 1 to n - 1 depending on status set earlier
        for col in range(1, n_cols):
            if matrix[0][col] == 0:
                for row in range(1 , n_rows):
                    matrix[row][col] = 0
        # zero out first row
        if row0 == 0:
            for col in range(n_cols):
                matrix[0][col] = 0 
        # zero out first column 
        if col0 == 0:
            for row in range(n_rows):
                matrix[row][0] = 0 
            
            
                
                
                    
                    
            
                
                
                    
                            
                            
                            
        
                    
        
                    
                            
        
