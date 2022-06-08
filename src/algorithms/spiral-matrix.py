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
        TL = [0, 0]
        TR = [0, len(matrix) - 1]
        BL = [len(matrix[0]) - 1, 0]
        BR = [len(matrix[0]) - 1, len(matrix) - 1]
        result = []
        for i in range(N):
            #seed = [TL[0] + i, TL[1] + i]            
            # 2.1. Print from TL + seed_x to TR - seed_x 
            a = TL[0] + i
            b = TR[0] - i
            row = i
            for j in range(a, b):
                result.append(matrix[row][j])
                
            # 2.2. Print from TR + seed_y  to BR - seed_y 
            a = TR[1] + i
            b = BR[1] - i
            col = len(matrix[0]) - 1 - i
            for j in range(a, b):
                result.append(matrix[j][col])

            # 2.3. Print from BR - seed_x to BL - seed_x 
            a = BR[0] - i
            b = BL[0] + i
            row = len(matrix) - 1 - i
            for j in range(a, b):
                result.append(matrix[row][j])

            # 2.4. Print from BL - seed_Y to TR - seed_Y 
            a = BL[1] - i
            b = TL[1] + i
            col = i
            for j in range(a, b):
                result.append(matrix[j][col])
                
        return result        
