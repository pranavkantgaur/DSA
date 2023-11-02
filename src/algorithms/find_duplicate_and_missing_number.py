# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
class Solution:
  def findNumbers(self, nums):
    current = 0
    duplicated = -1
    missing = -1
    # sort the array
    while(current < len(nums)):
      if nums[current] != current + 1:
        t = nums[nums[current] - 1]
        if t != nums[current]:
          nums[nums[current] - 1] = nums[current]
          nums[current] = t
        else:
          current += 1
      else:
        current += 1
    
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        duplicated, missing = nums[current], current + 1
        return [duplicated, missing]
      else:
        current += 1

    return [-1, -1]
