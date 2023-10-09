# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    dp = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    def get_01_count(self, str):
        l_1, l_2 = 0, 0
        for letter in str:
            if letter == '0':
                l_1 += 1
            if letter == '1':
                l_2 += 1
        return l_1, l_2            

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0 or (m == 0 and n == 0): return 0
        if self.dp[len(strs)][m][n] != -1: return self.dp[len(strs)][m][n]
        nzeros, nones = self.get_01_count(strs[0])
        if nzeros > m or nones > n:
            self.dp[len(strs)][m][n] = self.findMaxForm(strs[1:], m, n) # take/include is not feasible     
        else:
            include = 1 + self.findMaxForm(strs[1:], m - nzeros, n - nones) # [0, 1, 1], 1, 2 -> [1, 1], 0, 2 -> [1], 0, 1 -> [], 0, 0 ->     # update available budget if this take step is feasible.
            exclude = self.findMaxForm(strs[1:], m, n)
            self.dp[len(strs)][m][n] = max(include, exclude)
        return self.dp[len(strs)][m][n]
        '''
        1. Init dp array for single string        
        2. Use it to build dp array for bigger probs.
        3. return val dp[len(strs)][m][n]
        # bottom up:
        dp = [[[]]]
        for i in range(m):
            for j in range(n):
                nzeros, nones = self. get_01_count(strs[0])
                if nzeros <= m and nones <= n:
                    dp[1][i][j] = 1
        for len_id in range(len(str)):
            for i in range(m):
                for j in range(n):

        '''        
