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
        if m < 0 or n < 0: return 0
        if self.dp[len(strs)][m][n] != -1: return self.dp[len(strs)][m][n]
        nzeros, nones = self.get_01_count(strs[0])
        include = 1 + self.findMaxForm(strs[1:], m - nzeros, n - nones)
        exclude = self.findMaxForm(strs[1:], m, n)
        self.dp[len(strs)][m][n] = max(include, exclude)
        return self.dp[len(strs)][m][n]
