# https://leetcode.com/problems/jump-game/
'''
Base condition: if nextpos == lastpos: return True, if nextpos > lastpos: return false
for each nextpos in range(a[I]): if jumpgame(nextpos, lastpos): return true.   Outside for loop: return false
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0:
            return False
        if len(nums)==1:
            if nums[0] == 0:
                return True
            else:
                return False
        for k in range(1, nums[0] + 1): # evaluate all actions at this state
            if self.canJump(nums[k:]):
                return True
            else:
                continue
        return False                
