# https://leetcode.com/problems/unique-paths/
class Solution:
    def upUtils(self, m, n, upMap):
        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    upMap[row][col] = 1                
        for row in range(1, m):
            for col in range(1, n):
                upMap[row][col] = upMap[row - 1][col] + upMap[row][col - 1]
        return                
        
    def uniquePaths(self, m: int, n: int) -> int:
        upMap = [[] for row in range(m)]        
        for row in range(m):            
            upMap[row] = [0 for col in range(n)]
        self.upUtils(m , n, upMap)
        return upMap[m - 1][n - 1]
        
        
        
        
