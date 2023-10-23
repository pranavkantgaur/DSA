# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
import math

class Solution:
    def findLength(self, arr, k):
      max_length = 0
      left = 0
      right = 0
      freq_map = [0 for _ in range(2)]
      freq_map[arr[right]] += 1
      while(left <= right and right < len(arr)):        
        if freq_map[1] >= right - left + 1 - k:
          max_length = max(max_length, right - left + 1)
          if right < len(arr) - 1: # expanding window only in case if we have one soln
            right += 1
            freq_map[arr[right]] += 1
          else:
            break                    
        else: # assuming that it is because there is a smaller candidate in this window.
          freq_map[arr[left]] -= 1
          left += 1
                    
      return max_length
