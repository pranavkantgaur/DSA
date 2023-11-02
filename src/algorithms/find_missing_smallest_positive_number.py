# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Note: Positive numbers start from '1'.

class Solution:
  def findNumber(self, nums):
    # TODO: Write your code here
    '''
    1. put positive numbers at there index, assuming index 0 is for number 1 and so on
    2. ignore negative and outof aray length numbers
    3. after above ordering, visit the array
    4. return the index + 1 of the first element where nums[index] != index + 1    
    '''
    # sort array
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        if nums[current] <= 0 or nums[current] >= len(nums):
          current += 1
        else: # swap to place a number at its correct position
          t = nums[nums[current] - 1]
          if t != nums[current]:
            nums[nums[current] - 1] = nums[current]
            nums[current] = t
          else: # duplicate, ignore
            current += 1
      else:
        current += 1
    # look for smallest positive missing number
    current = 0
    while(current < len(nums)):
      if nums[current] != current + 1:
        return current + 1   
      current += 1

    return len(nums) + 1
