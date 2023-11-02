# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
class Solution:
  def findNumbers(self, nums, k):
    missingNumbers = []
    # sort the array
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        if nums[current] <= 0 or nums[current] > len(nums):
          current += 1
        else:
          t = nums[nums[current] - 1]
          if t != nums[current]:
            nums[nums[current] - 1] = nums[current]
            nums[current] = t
          else: # duplicate
            current += 1
      else:
        current += 1
    
    print('arr: ', nums)
    # search for k missing +ve numbers
    current = 0
    while(k > 0 and current < len(nums)):
      if nums[current] != current + 1:
        missingNumbers.append(current + 1)
        k -= 1
      current += 1
    return missingNumbers
