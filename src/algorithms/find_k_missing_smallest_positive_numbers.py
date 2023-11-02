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
          else:
            current += 1
      else:
        current += 1
    
    # search for k missing +ve numbers
    current = 0
    extraNums = set() # store numbers which are + and > len(nums), so as to avoid them being added as missing numbers later.
    while(current < len(nums) and k > 0):
      if nums[current] != current + 1:
        missingNumbers.append(current + 1)
        if nums[current] > len(nums):
          extraNums.add(nums[current])
        k -= 1
      current += 1

    missing_num_cand = len(nums) + 1
    while(k > 0):
      if missing_num_cand in extraNums:
        missing_num_cand += 1
      else:
        missingNumbers.append(missing_num_cand)
        k -= 1

    return missingNumbers
