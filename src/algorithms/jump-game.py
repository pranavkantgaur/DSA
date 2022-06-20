# https://leetcode.com/problems/jump-game/
'''
Base condition: if nextpos == lastpos: return True, if nextpos > lastpos: return false
for each nextpos in range(a[I]): if jumpgame(nextpos, lastpos): return true.   Outside for loop: return false
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for k in range(1, nums[0] + 1): # evaluate all actions at this state
            if k < len(nums):
                if self.canJump(nums[k:]):
                    return True
                else:
                    continue
            else:
                return False
        return False   
    
  class SolutionWithMemoization:      
    jM = {} # set this to -1 for all positions of input array
    
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:            
            return True
        if nums[0] == 0:
            return False
        for k in range(1, nums[0] + 1): # evaluate all actions at this state
            if k <= len(nums):
                if jM[k] != -1:
                    if jm[k] == 1:
                        jm[i] = 1
                        return True
                    else:
                        continue                    
                else:
                    jM[k] = self.canJump(nums, k, n)                    
            else:
                return False
        return False                
