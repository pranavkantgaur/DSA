# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
class Solution:
    def helper(self, n, dp):
        if n <= 2: 
            dp[n] = n
            return dp[n]
        for i in range(1, n):
            dp[n] = min(n if dp[n] == 0 else dp[n], 1 + max(i - 1, self.helper(n - i, dp)))
        return dp[n]

    def twoEggDrop(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        self.helper(n, dp)
        return dp[n]

        
        
