# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

class Solution:
  def searchCeilingOfANumber(self, arr, key):
    left = 0
    right = len(arr) - 1
    while(left <= right):
      mid = left + (right - left) // 2
      if arr[mid] > key:
        right = mid - 1
      elif arr[mid] < key:
        left = mid + 1
      else:
        return mid
    if left == len(arr):
      return -1
    else:
      return left     
