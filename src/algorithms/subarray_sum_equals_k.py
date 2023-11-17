# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hMap = {}
        cum_sum = 0
        subarray_count = 0
        for num in nums: # checking each index as a candidate for the right end of subarray of size k
            cum_sum += num
            if cum_sum - k in hMap: # get the count of subarray with sum = cum_sum - k, becuase we want to get count of subarrays with cum_sum - x = k condition, where x  = cum_sum - k
                subarray_count += hMap[cum_sum - k]
            if cum_sum not in hMap:
                hMap[cum_sum] = 0
            hMap[cum_sum] += 1
        if k in hMap: # if there were subarray from 0th index as the left index, then count them too.
            subarray_count += hMap[k]
        return subarray_count

        
