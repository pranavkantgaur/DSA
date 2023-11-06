# https://leetcode.com/problems/split-array-largest-sum/
class Solution:
    def isPartitionPossible(self, target_sum, arr, k):
        # check if it is possible to partition the array into k partitions with max sum of subarray being atmost k
        return is_possible

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while(left <= right):
            mid = left + (right - left) // 2
            if self.isPartitionPossible(mid, nums, k)
                right = mid - 1
        return left

        
