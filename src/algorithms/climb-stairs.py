# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairsUtil(self, n: int, cs_map) -> None:        
        for i in range(1, n + 1):
            if i <= 2:
                cs_map[i] = i
            else:
                cs_map[i] = cs_map[i - 1] + cs_map[i - 2]
    
    def climbStairs(self, n: int) -> int:
        # create the map
        cs_map = [-1 for i in range(n + 1)]
        self.climbStairsUtil(n, cs_map)
        return cs_map[n]
        
    
    
            
        
