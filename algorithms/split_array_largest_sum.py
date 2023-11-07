# https://leetcode.com/problems/split-array-largest-sum/
class Solution:    
    def predicate(self, target, k, nums):
        total = 0
        parts = 1
        for num in nums:
            total += num
            if total > target:
                total = num
                parts += 1
                if parts > k:
                    return False

        return True
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while(left < right):
            mid = left + (right - left) // 2
            if self.predicate(mid, k, nums):
                high = mid
            else:
                left = mid + 1
        return left        
        
