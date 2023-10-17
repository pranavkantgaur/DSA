# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
class Solution:
  def swap(self, arr, id1, id2):
    t = arr[id1]
    arr[id1] = arr[id2]
    arr[id2] = t
    return 
  def sort(self, arr):
    left = 0 # points to where last 0 should be
    right = len(arr) - 1 # points to where first 2 should be
    i = 0
    while(i <= right): 
      if arr[i] == 0: 
        self.swap(arr, i, left)
        left += 1
        i += 1
      elif arr[i] == 1:
        i += 1
      else: # 2
        self.swap(arr, i, right) 
        right -= 1
    return arr
