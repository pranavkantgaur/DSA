# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

class Solution:
  def findSubarrays(self, arr, target):
    result = []
    left = 0
    right = 0
    '''
    1. Iterate on each right indenx
    2. For each resulting left,right, check if thr prod < T 
    3. if prod >= t, squeeze the window untill the prod < T
    4. Once the prod < T, add all subarrays within it to the result list
    5. return result
    '''
    prod = 1.0
    while(right < len(arr)):
      prod *= arr[right]
      while(prod >= target and left < len(arr)): # purge invalid candidates
        prod /= arr[left]
        left += 1
      # now we have a candidate window
      i = right
      while(i >= left):
        result.append(arr[i:right + 1])        
        i -= 1
      right += 1        
    return result
