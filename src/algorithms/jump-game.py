# https://leetcode.com/problems/jump-game/
class Solution:      
    def jgUtil(self, start, end, nums, jg_map):
        if start ==  end:
            jg_map[start] =  1 # true
            return True
        if nums[start] == 0:
            jg_map[start] = 0
            return False
        for action in range(1, nums[start] + 1):
            if action + start <= end:
                if jg_map[action + start] == 1:
                    jg_map[start] = 1
                    return True
                elif jg_map[action + start] == 0:
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
        jg_map = [-1] * len(nums) #set to all -1s for len(nums), TODO
        # REFER: https://stackoverflow.com/questions/1298636/how-to-set-initial-size-for-a-dictionary-in-python
        start = 0
        end = len(nums) - 1
        return self.jgUtil(start, end, nums, jg_map)
