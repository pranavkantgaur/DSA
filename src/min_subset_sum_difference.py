# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
class Solution:
  
  def helper(self, start_id, current_sum, min_diff, arr, dp):
    if start_id <= len(arr): # valid state?
      if dp[start_id][current_sum] != -1: # already solved?
        return
      else:
        if start_id == len(arr): # base case?
          include_diff = abs(sum(arr) - 2 * current_sum + arr[start_id - 1])
          exclude_diff = abs(sum(arr) - 2 * current_sum)
          dp[start_id][current_sum] = min(min_diff, include_diff, exclude_diff)
        else:
          if dp[start_id + 1][current_sum + arr[start_id - 1]] == -1: # include problem solved?
            self.helper(start_id + 1, current_sum + arr[start_id - 1], min_diff, arr, dp)
          include_diff = dp[start_id + 1][current_sum + arr[start_id - 1]]
          if dp[start_id + 1][current_sum] == -1: # exclude problem solved?
            self.helper(start_id + 1, current_sum, include_diff, arr, dp)
          exclude_diff = dp[start_id + 1][current_sum]
          dp[start_id][current_sum] = exclude_diff
        return
    else:
      return

  def canPartition(self, num):
    dp = [[-1 for _ in range(sum(num) + 1)] for _ in range(len(num) + 1)]
    self.helper(1, 0, sum(num), num, dp)
    return dp[1][0]
    
