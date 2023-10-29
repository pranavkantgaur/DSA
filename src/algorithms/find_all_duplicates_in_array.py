# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        offset = len(nums)
        n = len(nums)
        for num in nums:
            if num <= n: # to avoid out of index
                id = num - 1
            else:
                id = num - offset - 1
            if nums[id] > n: # visited once, repated 2 times
                result.append(id + 1)
            else:
                nums[id] += offset
        return result
  
        
        
