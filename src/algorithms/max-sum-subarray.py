# https://leetcode.com/problems/maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
        '''
        if max(nums) < 0:
            return max(nums)
        '''
        max_sum_so_far = min(nums) - 1
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            if sum_so_far > max_sum_so_far:
                max_sum_so_far = sum_so_far
            if sum_so_far < 0:
                sum_so_far = 0
        return max_sum_so_far      
