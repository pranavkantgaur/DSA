# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.
class Solution:
  def searchMinDiffElement(self, arr, key):
    left = 0
    right = len(arr) - 1
    while(left <= right):
      mid = left + (right - left) // 2
      if arr[mid] > key:
        right = mid - 1
      elif arr[mid] < key:
        left = mid + 1
      else:
        return arr[mid]
    if right == -1 or (left != len(arr) and abs(arr[left] - key) < abs(arr[right] - key)):
      return arr[left]
    else:
      return arr[right]
