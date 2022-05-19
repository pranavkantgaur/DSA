# https://leetcode.com/problems/permutations/'''
'''
Approach 1:
1. For each number in the nums list:
   1.1. Set that number as the first number of the permutation and permute remaining numbers
        1.1.1 Recursively do this untill the nums size is 2 when you can return with [nums[0], nums[1]] and [nums[1], nums[0]]
'''
class Solution:
    results = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            for num in nums:         
                next_nums = nums.copy()
                next_nums.remove(num)
                #print("Next nums: ", next_nums, nums)
                permutation_result = self.permute(next_nums) # since numbers are distinct
                #print('RESULT: ', permutation_result)
                for result in permutation_result:                                        
                    result.insert(0, num)
                    self.results.append(result)    
            return self.results                
        
        
