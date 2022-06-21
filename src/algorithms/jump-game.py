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
    def jgUil(self, start, end, nums, jg_map):
        if start ==  end:
            jg_map[start] =  1 # true
            return True
        if nums[start] == 0:
            jg_map = 0
            return False
        for action in range(1, nums[start] + 1):
            if action + start <= end:
                if jg_map[action + start] == 1:
                    jg_map[start] = 1
                    return True
                if jg_map[action + start] == 0:
                    continue
                else:
                    if self.jgUtil(start + action, end, nums, jg_map) == True:
                        jg_map[start] = 1
                        return True
                    else:
                        continue
            else:
                break
        return False            
                    
    
    def canJump(self, nums: List[int]) -> bool:
        jg_map = {} #set to all -1s for len(nums), TODO
        self.jgUtil(start, end, nums, jg_map)
                
