# https://leetcode.com/problems/jump-game/
# https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C%2B%2B
class Solution:                     
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) # 5
        reach = 0
        i = 0
        for i in range(n): # [0, 1, 2, 3, 4]
            #print(i)
            if  i <=  reach: # 0 <= 
                reach = max(i + nums[i], reach)
            else:
                break
        print('val: ', i)
        return i == n - 1            
        

