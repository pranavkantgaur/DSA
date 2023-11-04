# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
class Solution:
  def search(self,arr, key):
    '''
    1. check if list is ascending/descending
    2. binary search accordingly
    '''
    left = 0
    right = len(arr) - 1
    if arr[0] > arr[-1]: # descending
      while(left < right):
        mid = left + (right - left) // 2
        if arr[mid] > key:
          left = mid + 1
        if arr[mid] < key:
          right = mid - 1
        else:
          return mid
    elif arr[0] < arr[-1]: # ascending
        while(left < right):
          mid = left + (right - left) // 2
          if arr[mid] > key:
            right = mid - 1
          if arr[mid] < key:
            left = mid + 1
          else:
            return mid
    else:
      if arr[0] == key:
        return 0
    return -1  # element not found
