# https://leetcode.com/problems/subsets-ii/
class Solution:    
    
    def sub(self, nums, current_subs, result):
        if len(nums) == 0:
            if not self.subs_exists(current_subs, result):
                result.append(current_subs)
            #current_subs = []
        if len(nums) == 1:            
            if not self.subs_exists(current_subs, result):
                result.append(current_subs)
            current_subs.append(nums[0])            
            if not self.subs_exists(current_subs, result): # Bottleneck
                result.append(current_subs)
            #current_subs = []
        
        # exclude;
        self.sub(nums[1:], current_subs, result)
        # include        
        current_subs.append(nums[0])
        self.sub(nums[1:], current_subs, result)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        BF: TC: O(2^2n), SC: O(n * 2^n)        
        '''
        result = []
        current_subs = []
        self.sub(nums, current_subs, result)
        return result
