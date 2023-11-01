# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. 
# Write a function to sort the objects in-place on their creation sequence number in O(n) and without using any extra space. 
class Solution:
  def sort(self, nums):
    current = 0
    while(current < len(nums)):
      if nums[current] == current + 1: # already sorted
        current += 1
      else:
        t = nums[nums[current] - 1]
        nums[nums[current] - 1] = nums[current]
        nums[current] = t        
    return nums
