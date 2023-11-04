# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

class Solution:
  def findRange(self, arr, key):
    leftmost = -1
    rightmost = -1
    # search for left most key
    left = 0
    right = len(arr) - 1

    while(left <= right):
      mid = left + (right - left) // 2
      if arr[mid] > key:
        right = mid - 1
      elif arr[mid] < key:
        left = mid + 1
      else:
        leftmost = mid
        right = mid - 1

    # search for right most key
    left = 0
    right = len(arr) - 1

    while(left <= right):
      mid = left + (right - left) // 2
      if arr[mid] > key:
        right = mid - 1
      elif arr[mid] < key:
        left = mid + 1
      else:
        rightmost = mid
        left = mid + 1
    
    return [leftmost, rightmost]

