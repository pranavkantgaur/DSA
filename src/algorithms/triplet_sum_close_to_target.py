# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    arr.sort()
    result = max(arr) * 3 + 1
    min_diff = max(arr) * 3 + 1 # TODO reasonable value?
    for i, num in enumerate(arr):
      left = i + 1
      right = len(arr) - 1      
      while(left < right):
        current_sum = num + arr[left] + arr[right]
        current_diff = current_sum - target_sum
        if current_diff < 0:
          left += 1                      
        elif current_diff > 0:
          right -= 1
        else:
          return 0            
        if abs(min_diff) > abs(current_diff): # a closer triplet is found
          min_diff = current_diff
          result = current_sum           
        elif abs(min_diff) == abs(current_diff):
          if current_diff < 0:
            result = current_sum         

    return result
