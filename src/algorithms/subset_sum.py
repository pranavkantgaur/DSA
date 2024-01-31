# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
class Solution:
  def helper(self, start_id, target_sum, dp):
    if target_sum == 0: 
      dp[start_id][target_sum] = 1
      return 1
    if target_sum < 0:
      return 0
    if dp[start_id][target_sum] == -1:
      if target_sum - arr[start_id] >= 0 and dp[start_id + 1][target_sum - arr[start_id]] != -1:
        include = dp[start_id + 1][target_sum - arr[start_id]]
      else:
        include = self.helper(start_id + 1, target_sum - arr[start_id], dp)
      exclude = dp[start_id + 1][target_sum]
      if include == 0 and dp[start_id + 1][target_sum] == -1:
        exclude = self.helper(start_id + 1, target_sum, dp)
      dp[start_id][target_sum] = include or exclude
    return dp[start_id][target_sum]  
  def canPartition(self, num, sum):
    dp = [[-1 for _ in range(sum + 1)] for _ in range(len(num) + 1)]
    self.helper(0, 0, dp)
    return dp[0][0] == 1
