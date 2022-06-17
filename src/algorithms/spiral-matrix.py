# https://leetcode.com/problems/spiral-matrix/
'''
1. Set TL = [0,0], TR=[0, m-1], BL = [n - 1, 0], BR=[n-1, m-1]
2. For i from 1 to X:
   2.0  Set seed from i 
   2.1. Print from TL + seed_x to TR - seed_x 
   2.2. Print from TR + seed_y  to BR - seed_y 
   2.3. Print from BR - seed_x to BL - seed_x 
   2.4. Print from BL - seed_Y to TR - seed_Y 
   
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1
        result = []
        while(rowStart <= rowEnd and colStart <= colEnd):
            print(rowStart, rowEnd, colStart, colEnd)
            for i in range(colStart, colEnd + 1): # Towards right
                result.append(matrix[rowStart][i])
            rowStart += 1
            for j in range(rowStart, rowEnd + 1): # towards bottom                
                result.append(matrix[j][colEnd])
            colEnd -= 1
            if rowStart <= rowEnd:                
                for k in range(colEnd, colStart - 1, -1): # towards left
                    result.append(matrix[rowEnd][k])
            rowEnd -= 1             
            if colEnd >= colStart:                
                for x in range(rowEnd, rowStart - 1, -1): # towards top
                    result.append(matrix[x][colStart])
            colStart += 1      
   
        return result                
