# https://leetcode.com/problems/ones-and-zeroes/
# https://leetcode.com/problems/ones-and-zeroes/

class Solution:
    dp = [[[-1 for _ in range(101)] for _ in range(101)] for _ in range(601)]
    def get_01_count(self, str):
        l_1, l_2 = 0, 0
        for letter in str:
            if letter == '0':
                l_1 += 1
            if letter == '1':
                l_2 += 1
        return l_1, l_2            

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        for m_i in range(m):
            for n_i in range(n):
                self.dp[0][m_i][n_i] = 0
        zero_one_counts = [(s.count('0'), s.count('1')) for s in strs]
        for i in range(1, len(strs) + 1):
            for m_i in range(m + 1):
                for n_i in range(n + 1):
                    if zero_one_counts[i - 1][0] >= m_i and zero_one_counts[i - 1][1] >= n_i:
                        self.dp[i][m_i][n_i] = max(self.dp[i - 1][m_i][n_i], self.dp[i - 1][m_i - zero_one_counts[i - 1][0]][n_i - zero_one_counts[i - 1][1]])
                    else:
                        self.dp[i][m_i][n_i] = self.dp[i - 1][m_i][n_i]
        return self.dp[len(strs)][m][n]  
        
        
        '''
        top-down memoization
        if len(strs) == 0 or (m == 0 and n == 0): return 0
        if self.dp[len(strs)][m][n] != -1: return self.dp[len(strs)][m][n]
        
        exclude = self.findMaxForm(strs[1:], m, n) # 1 - 2, 2, e = 0

        nzeros, nones = self.get_01_count(strs[0]) # n0=0, n1 = 1
        if nzeros > m or nones > n:
            self.dp[len(strs)][m][n] = exclude
        else:
            include = 1 + self.findMaxForm(strs[1:], m - nzeros, n - nones) # i = 0
            self.dp[len(strs)][m][n] = max(include, exclude) # dp[1][2][2] = 0
        return self.dp[len(strs)][m][n]
        
        
        #bottom-up
        for m_i in range(m):
            for n_i in range(n):
                dp[0][m_i][n_i] = 0
        n_zeros = [count for s in strr]
        n_ones = [count for s in strr]
        for i in range(1, len(strs) + 1):
            for m_i in range(m + 1):
                for n_i in range(n + 1):
                    if n_zeros >= m_i and n_ones >= n_i:
                        dp[i][m_i][n_i] = max(dp[i - 1][m_i][n_i], dp[i - 1][m_i - n_zeros][n_i - n_ones])
                    else:
                        dp[i][m_i][n_i] = dp[i - 1][m_i][n_i]
        return dp[len(strs)][m][n]  
        '''
