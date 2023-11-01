# We are given an array containing n distinct numbers taken from the range 0 to n. Since the array has only n numbers out of the total n+1 numbers, find the missing number.
class Solution:
  def findMissingNumber(self, nums):
    n = len(nums)
    current = 0
    while(current < n):
      if nums[current] == current or nums[current] == n:
        current += 1
      else:
        t = nums[current]
        nums[current] = nums[t]
        nums[t] = t
    
    current = 0
    while(current < n):
      if nums[current] != current:
        return current
      else:
        current += 1
    return n
    

