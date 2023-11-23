# https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0
        cum_sum = 0
        min_len = len(nums) + 1        
        left = 0
        right = 0
        while(right < len(nums)):
            cum_sum += nums[right]                
            while(left <= right and cum_sum >= target):                
                min_len = min(min_len, right - left + 1)
                cum_sum -= nums[left]
                left += 1
            right += 1
        
        return min_len
        
