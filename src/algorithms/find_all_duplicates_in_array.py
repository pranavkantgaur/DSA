# https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
  def findNumbers(self, nums):
    duplicateNumbers = []
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        t = nums[nums[current] - 1]
        if t != nums[current]:
          nums[nums[current] - 1] = nums[current]
          nums[current] = t
        else:
          duplicateNumbers.append(t)
          current += 1
      else:
        current += 1
    return duplicateNumbers
  
        
        
