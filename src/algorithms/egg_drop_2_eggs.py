# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n <= 2: return n
        drops = n
        for i in range(1, n):
            drops = min(drops, max(1 + i - 1, 1 + self.twoEggDrop(n - i)))
        return drops

        
