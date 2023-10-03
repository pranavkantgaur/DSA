# https://www.geeksforgeeks.org/minimum-length-unsorted-subarray-sorting-which-makes-the-complete-array-sorted/
import math

class Solution:
  def sort(self, arr):
    # TODO: Write your code here    
    #for i, num in enumerate(arr[]):
    i = 1
    while(i < len(arr)):
      if arr[i] < arr[i - 1]:
        left = i-1          
        break
      i += 1        

    i = len(arr) - 1
    while(i > 0):
      if arr[i - 1] > arr[i]:
        right = i
        break
      i -= 1        
    
    #sorted(nums[left: right + 1])    

    min_elem = min(arr[left: right+1])
    max_elem = max(arr[left: right+1])

    #if min_elem < arr[left - 1]:
      # update left
    while(left > 0 and min_elem < arr[left - 1]):
      left -= 1      
    while(right < len(arr) - 1 and max_elem > arr[right + 1]):
      right += 1      

    # if a num in this subarray is smaller/greater than a number outside this subarray then
    # l > right-left + 1, how to detect this? also compute max, min and expand the subarray accordingly
    # if min < arr[left - 1] then expand the subarray to left, left -= 1
    # if max > arr[right + 1] then expand subarray to right, right += 1
    # update l = right - left + 1
    l = right - left + 1    

    return l
