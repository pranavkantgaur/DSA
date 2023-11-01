# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.
class Solution:
  def findNumbers(self, nums):
    missingNumbers = []
    # sort the array
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        t = nums[nums[current] - 1]
        if t != nums[current]:
          nums[nums[current] - 1] = nums[current]
          nums[current] = t
        else: # ignore the duplicates
          current += 1          
      else:
        current += 1
    
    # look for missing numbers
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        missingNumbers.append(current + 1)
      current += 1

    return missingNumbers
