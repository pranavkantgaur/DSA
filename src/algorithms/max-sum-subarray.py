# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = 0
        max_sum_so_far = min(nums) - 1
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum < nums[i]:
                cum_sum = nums[i]
            max_sum_so_far = max(max_sum_so_far, cum_sum)
        return max_sum_so_far            
        
