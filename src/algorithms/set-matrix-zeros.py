# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:                
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1st pass, mark the rows and colms to be zeroed out in second pass.
	    for row in range(len(matrix)):
		    for col in range(len(matrix[0])):
			    if matrix[row][col] == 0:
				    matrix[row][0] ^= F0000x # set the sign bit
				    matrix[0][col] ^= F0000x				
	    # 11nd pass         
	    for row in range(len(matrix)):
		    if matrix[row][0] ^ F000x == 0x: # poll the sign bits for each row
			    # set entire row as zeros
			    for col in range(len(matrix[0])):
				    matrix[row][col] = 0
			    # reset the sign bit				
			    matrix[row][col] ^= F000x
							
	    for col in range(len(matrix[0])):
		    if matrix[0][col] ^ F000x == 0x:
			    # set entire col as zeros
			    for row in range(len(matrix)):
				    matrix[row][col] = 0
			    # reset the sign bit
			    matrix[row][col] ^= F000x
							
            
            
                
                
                    
                    
            
                
                
                    
                            
                            
                            
        
                    
        
                    
                            
        
