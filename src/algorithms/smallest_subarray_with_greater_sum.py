# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.
import math

class Solution:
  def findMinSubArray(self, s, arr):
    # TODO: Write your code here
    window_start = 0
    window_end = 0
    min_window_size = len(arr) + 1
    window_sum = arr[0]
    while(not(window_sum < s and window_end == len(arr) - 1)): # TODO: fix      
      
      if  window_sum >= s:
        # shrink the window
        while(window_start <= window_end and window_sum >= s):
          if window_end - window_start + 1 < min_window_size:
            min_window_size = window_end - window_start + 1
          # bookkeeping
          window_sum -= arr[window_start]
          window_start += 1        

      else: # expand
        window_end += 1  
        window_sum += arr[window_end]

    if min_window_size == len(arr) + 1: # no solution found
      min_window_size = 0
    return min_window_size
    '''
    1. start with window size 1
    2. grow window if sum is < s, 
    3. continue shrinking window untill sum > s and update min window size 
    4. after while loop, return the min_length seen so far
    '''
