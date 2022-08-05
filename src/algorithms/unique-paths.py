# https://leetcode.com/problems/unique-paths/
class Solution:
    def upUtils(self, m, n, upMap):
        if m == 1 or n == 1:
            upMap[m][n] = 1
            return 
        for row in range(m):
            for col in range(n):
                upMap[m][n] = upMap[m - 1][n] + upMap[m][n - 1]
        return                
        
    def uniquePaths(self, m: int, n: int) -> int:
        upMap = [[] for row in range(m)]        
        for row in range(m):            
            upMap[row] = [-1 for col in range(n)]
            print('LenL ', len(upMap[row]))
        self.upUtils(m , n, upMap)
        return upMap[m][n]
        
        
