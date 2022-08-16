# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col] == 0:
                    j = 0
                    while(j < col):
                        matrix[row][j] = 0
                        j += 1
                    i = 0                    
                    while(i < row):
                        matrix[i][col] = 0
                        i += 1                                              
                else:
                    if col - 1 >= 0 and matrix[row][col - 1] == 0:
                            matrix[row][col] = 0
                    if row - 1 >= 0 and matrix[row - 1][col] == 0:
                            matrix[row][col] = 0
                    else:
                        continue                            

                    
        
