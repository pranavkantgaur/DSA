# https://leetcode.com/problems/jump-game/
# https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C%2B%2B
class Solution:                     
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        reach = 0
        i = 0
        for i in range(n): 
            if  i <=  reach: # 0 <= 
                reach = max(i + nums[i], reach)
            else:
                break
        return i <= reach and i == n - 1 # to avoid cases where i > reach at last element of nums           
        
        
        

