# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
class Solution:  
  def canPartition(self, num):
    if len(num) == 1: return num[0]
    dp = [-1 for _ in range(sum(num) + 1)]
    for start_id in range(len(num), 0, -1):
      current_sum_range = sum(num[:start_id - 1])
      for current_sum in range(current_sum_range):
        if start_id == len(num):
          include_diff = abs(sum(num) - 2 * (current_sum + num[start_id - 1]))
          exclude_diff = abs(sum(num) - 2 * current_sum)
        else:
            include_diff = dp[current_sum + num[start_id - 1]]
            exclude_diff = dp[current_sum]
        dp[current_sum] = min(include_diff, exclude_diff)
    return dp[0]
