# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
  def findNumber(self, nums):
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        t = nums[nums[current] - 1]
        if t == nums[current]: # duplicate
          return nums[current]
        else: # swap
          nums[nums[current] - 1] = nums[current]          
          nums[current] = t
      else: # number already at right place
        current += 1          
    return -1

                        
        
