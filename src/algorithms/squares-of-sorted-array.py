# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [pow(num, 2) for num in nums]
        return sorted(nums)
        
