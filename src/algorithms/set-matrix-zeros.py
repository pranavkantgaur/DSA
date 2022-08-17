# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        is_seed = [[] for row in range(n_rows)]
        for row in range(n_rows):
            is_seed[row] = [1 for col in range(n_cols)]
        
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0:
                    j = 0
                    while(j < col):
                        matrix[row][j] = 0
                        is_seed[row][j] = 0
                        j += 1
                    i = 0                    
                    while(i < row):
                        matrix[i][col] = 0
                        is_seed[i][col] = 0
                        i += 1                                              
                else:
                    if row == 1 and col == 2:
                        print(f'so far: {is_seed}')
                        print(f'check: {matrix[row][col - 1]}')
                        print(f'also: {is_seed[row][col - 1]}')
                    if col - 1 >= 0 and matrix[row][col - 1] == 0 and is_seed[row][col - 1] == 1:
                            matrix[row][col] = 0
                            is_seed[row][col] = 0
                    if row - 1 >= 0 and matrix[row - 1][col] == 0 and is_seed[row - 1][col] == 1:
                            matrix[row][col] = 0 
                            is_seed[row][col] = 0

                    
                            
        
