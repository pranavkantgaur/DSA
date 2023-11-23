# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        #Map = Collections.counter(nums[:k])
        hMap = {}
        for i in range(k):
            if nums[i] in hMap.keys():
                hMap[nums[i]] += 1    
            else: 
                hMap[nums[i]] = 1
        if len(hMap) == k:
            max_sum = sum(nums[:k])
        sub_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            sub_sum += nums[i]
            if nums[i] in hMap:
                hMap[nums[i]] += 1
            else:
                hMap[nums[i]] = 1
            hMap[nums[i - k]] -= 1
            sub_sum -= nums[i - k]
            if hMap[nums[i-k]] == 0: del hMap[nums[i - k]]
            if len(hMap) == k:
                max_sum = max(max_sum, sub_sum)
        return max_sum     
