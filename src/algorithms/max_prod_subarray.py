# https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        1. Compute prefix array and suffix prod array
        2. update ax rod as max(max, prefix, suffix)
        '''
        l = 1
        r = 1
        max_so_far = min(nums) - 1
        for i in range(len(nums)):
            if nums[i] != 0:
                l *= nums[i]
            else:
                l = 1
            if nums[~i] != 0:
                r *= nums[~i]
            else:
                r = 1
            if nums[i] != 0 and nums[~i] != 0:
                max_so_far = max(max_so_far, l, r)
                #print('Hi')
            else:
                if nums[i] == 0 and nums[~i] != 0:
                    max_so_far = max(max_so_far, 0, r)
                elif nums[i] != 0 and nums[~i] == 0:
                    max_so_far = max(max_so_far, l, 0) 
                else:
                    max_so_far = max(max_so_far, 0)           
        return max_so_far
