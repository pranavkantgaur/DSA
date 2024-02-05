# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
class Solution:  
     
  def helper(self, start_id, arr, target_sum, dp):
    if start_id > len(arr) or target_sum < 0: return # invalid states
    if target_sum == 0: # solved state
      dp[start_id][target_sum] = 1
      return
    if dp[start_id][target_sum] == -1: # unsolved valid state
      if start_id < len(arr):
        include_target_sum = target_sum - arr[start_id]            
        if include_target_sum >= 0: # include state is valid
          if dp[start_id + 1][include_target_sum] == -1: # include state solved?
            self.helper(start_id + 1, arr, include_target_sum, dp)
          include = dp[start_id + 1][include_target_sum]
        else:
          include = 0            
        if include == 0: # solve exclude only then
          if dp[start_id + 1][target_sum] == -1: # exclude state solved?
            self.helper(start_id + 1, arr, target_sum, dp)
          exclude = dp[start_id + 1][target_sum]
        else: # dont care about exclude state solution
          exclude = 0
        # use include and exclude to solve current state
        dp[start_id][target_sum] = include or exclude
      else: # include and exclude states are invalid.
        dp[start_id][target_sum] = 0
    return
  
  def canPartition(self, num, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(len(num) + 1)]
    return self.helper(0, num, sum, dp)
