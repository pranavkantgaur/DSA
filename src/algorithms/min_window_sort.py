# https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
import math

import math

class Solution:
  def sort(self, arr):
    '''
    1. Locate the window with flipped endpoint
    2. grow the window on both ends unless no anamoly is left
        1. do left -= 1 if arr[left] > min_element_in_window
        2. do right += 1 if arr[right] < max_element_in_window
    3. return the window size.
    '''
    left = 0
    right = len(arr) - 1
    l = 0
    while(left < len(arr) - 1 and arr[left] <= arr[left + 1]):
      left += 1
    while(right > 0 and arr[right] >= arr[right - 1]):
      right -= 1
      
    if left < right:
      min_element = min(arr[left:right + 1])                  
      max_element = max(arr[left: right + 1])

      while(left > 0 and arr[left - 1] > min_element):
        left -= 1
      while(right < len(arr) - 1 and arr[right + 1] < max_element):
        right += 1           

      l = right - left + 1
    return l
