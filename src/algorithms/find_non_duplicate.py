'''
Given an array of sorted numbers, move all non-duplicate number instances at the beginning of the array in-place. The relative order of the elements should be kept the same and you should not use any extra space so that the solution has constant space complexity i.e.,
Move all the unique number instances at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.
'''
class Solution:
  def remove(self, arr):
    current, end = 0, 0
    while(current < len(arr) - 1):
      if arr[current] < arr[current + 1]:
        if current > end + 1:
          t = arr[end + 1]
          arr[end + 1] = arr[current]
          arr[current] = arr[t]
          end += 1
        else:
          end += 1        
      current += 1
    return end + 1
