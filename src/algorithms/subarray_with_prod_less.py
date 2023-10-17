# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.

class Solution:
  def findSubarrays(self, arr, target):
    result = []
    # TODO: Write your code here
    '''
    1. start  =0, end  = 0
    2. grow the window untill prod < t
    3. once prod >= t, start += 1 : add all subarrays between start-end
    4. repeat 2-3 untill end <= len(arr) - 1
    '''
    start = 0
    end = 0
    prod = 1
    result = []
    while(end <= len(arr) - 1):
      prod *= arr[end]
      if prod < target:
        result.append(arr[start:end + 1])  
        end += 1
      else:
        prod /= arr[start]  # TODO: divide by 0, if 1st num > target          
        start += 1
        for last_id in range(start, end+1):          
          result.append(arr[start:last_id+1])
        end += 1                  
        
    return result
