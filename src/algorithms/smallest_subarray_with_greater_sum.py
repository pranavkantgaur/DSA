# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if no such subarray exists.
import math

class Solution:
  def findMinSubArray(self, s, arr):
    '''
    1. start with 1-size window
    2. for each end index of window, update current window sum
    3. if window sum is greater than target, update min_length and attempt to get even better solution with same end index
    4. move to next end index
    5. return min length seen so far as solution.
    '''
    start = 0
    min_length = len(arr) + 1
    wind_sum = 0
    for end in range(len(arr)):
      wind_sum += arr[end]
      while(wind_sum >= s):
        min_length = min(min_length, end - start + 1)         
        wind_sum -= arr[start]
        start += 1
    if min_length == len(arr) + 1:
      min_length = 0
    return min_length      
