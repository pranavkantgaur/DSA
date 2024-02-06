# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.
class Solution:   
  def canPartition(self, num, sum):
    dp = [-1 for _ in range(sum + 1)]
    for start_id in range(len(num), 0, -1):
      for target_sum in range(sum, -1, -1):
        if target_sum == 0:
          dp[target_sum] = 1
          continue        
        if start_id == len(num):          
          if target_sum - num[start_id - 1] == 0: 
            dp[target_sum] = 1
          else:
            dp[target_sum] = 0
          continue
        # other states
        include = 0
        include_target_sum = target_sum - num[start_id - 1]
        if include_target_sum >= 0: 
          include = dp[include_target_sum]        
        exclude = 0
        if include == 0:
          exclude = dp[target_sum]
        dp[target_sum] = include or exclude
    return dp[sum] == 1
