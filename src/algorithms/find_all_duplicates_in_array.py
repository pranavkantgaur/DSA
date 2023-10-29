# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        offset = len(nums)
        for num in nums:
            nums[(num - 1) % len(nums)] += offset
        for num in nums:
            if (nums[(num - 1) % len(nums)] // offset) == 2:
                result.append((num - 1) % len(nums))
        return result  
        
