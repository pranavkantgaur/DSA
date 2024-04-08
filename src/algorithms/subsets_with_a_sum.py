class Solution:  
  def countSubsets(self, num, sum1):
    #return self.helper(0, sum1, 0, num) # [1, 1, 2, 3], 4 => 3
    dp = [-1 for _ in range(sum1 + 1)]
    for start_id in range(len(num), 0, -1):
      for target_sum in range(sum1, -1, -1):
        if target_sum == 0:
          dp[0] = 1
          continue
        if start_id == len(num):
          if target_sum - num[start_id - 1] == 0:
            dp[target_sum] = 1
          else:
            dp[target_sum] = 0
        else:
          if target_sum - num[start_id - 1] >= 0:
            dp[target_sum] = dp[target_sum - num[start_id - 1]] + dp[target_sum]    
          else:
            dp[target_sum] = dp[target_sum]
    return dp[sum1]
                                                                                          
