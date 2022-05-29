# https://leetcode.com/problems/rotate-image
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if i != j:
                    #print('sgdfg')
                    t = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = t
              
        for i in range(len(matrix)):
            left = 0
            right = len(matrix) - 1
            while(left < right):
                t = matrix[i][left]
                matrix[i][left] = matrix[i][right]
                matrix[i][right] = t
                left += 1
                right -= 1
          
        #print(matrix)
        return matrix        
