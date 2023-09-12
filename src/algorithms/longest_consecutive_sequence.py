'''
# https://leetcode.com/problems/longest-consecutive-sequence/
Clarify:
1. Possible to not to have anmy solution? No

Naive algorithm:TC: O(nlogn), SC: O(1)
1. Sort the array
2. Find out the consecutive subarrays:
   1. Check the difference of succesive numbers, if it is 1, then set the start pointer to the current number
   2. Continue to increment the end pointer untill the difference between successive numbers is 1
   3. Once the condition violates, update the max_length_consecutive_sequence
   4. Go to 1,untill end of array is not reached by end pointer.
3. Return the length of the longest subaray

def func(arr):
  arr = sorted(arr)	
  max_len = -1
  start = 0
  end = 0   
  i = 0  
   while(end < len(arr)):
    while(nums[i+1] - nums[i] == 1):
      end += 1
      i += 1
    if max_len < end - start:
      max_len = end - start
    i += 1
    start = i # reset start and end
    end = i	
'''
