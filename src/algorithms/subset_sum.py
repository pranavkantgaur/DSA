# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
class Solution:  
  def helper(self, start_id, arr, target_sum):    
    if target_sum == 0: return True
    if target_sum < 0: return False
    if start_id == len(arr): return False
    include = self.helper(start_id + 1, arr, target_sum - arr[start_id])
    exclude = self.helper(start_id + 1, arr, target_sum)
    return include or exclude
  
  def canPartition(self, num, sum):
    return self.helper(0, num, sum)
