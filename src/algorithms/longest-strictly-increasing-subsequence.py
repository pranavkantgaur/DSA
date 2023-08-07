'''
https://leetcode.com/problems/longest-increasing-subsequence/

1. Brute-force approach:
  1.1. For each subsequence of integer array:
       1.1.1. If it is a strictly increasing subsquence:
              1.1.1.1. Update the max subsequence length
       1.1.2. Else: continue              
2. Take or not-take approach: (TODO)   
    2.1. Given nums array:
        2.1.0. If the length of array is 1: return 1 as the solution # base condition
        2.1.1. a = Pick next element to be part of candidate solution and recursively call for sub-problem solution: a = 1 + subprob(arr[1:], last_elem = arr[0])
        2.1.2. b = Drop next element and recursively call for sub-problem solution: b = subprob(arr[1: ], last_elem = last_elem) # not updating the last elem. with arr[0]
    2.2. Select the max of a, b and return as output
           

'''


class Solution:
  def helper(nums, current_right_most_number, length, max_length_so_far):
    if len(nums) == 1:
      if current_right_most_number < nums[0]:
        length += 1
        if max_length_so_far < length:
          max_length_so_far = length
else:
  if nums[]
  
  def lengthOfLIS(self, nums: List[int]) -> int:
      self.helper(nums[1:], current_right_most_number, length + 1, max_length_so_far)
