class Solution:  
  # recursive impl.
  def helper1(self, start_id, target_sum, count, num):    
    if target_sum == 0:
      return count + 1
    if start_id == len(num) or target_sum < 0: # invalid state?
      return count 
    include_count = self.helper(start_id + 1, target_sum - num[start_id], count, num) # (1, 3, 0, num) -> (2, 2, 0, num) 
    exclude_count = self.helper(start_id + 1, target_sum, include_count, num) # (3, 2, 1, num) 1 -> 3 (4, 2, 1, num) = 1
    return exclude_count
  # top down impl.
  def helper2(self, start_id, target_sum, arr, dp): # [1, 1, 2, 3], t = 4:     
    if start_id <= len(arr) and target_sum >= 0: # valid state 
      if dp[start_id][target_sum] != -1: return # already solved
      else: # solve
        if target_sum == 0: # boundary case 1
          dp[start_id][0] = 1
          return
        if start_id == len(arr): # boundary case 2
          if target_sum - arr[start_id - 1] == 0:
            dp[start_id][target_sum] = 1
          else: 
            dp[start_id][target_sum] = 0            
          return  
        self.helper2(start_id + 1, target_sum - arr[start_id - 1], arr, dp) 
        self.helper2(start_id + 1, target_sum, arr, dp) 
        if target_sum - arr[start_id - 1] < 0:            
          dp[start_id][target_sum] = dp[start_id + 1][target_sum] 
        else:
          dp[start_id][target_sum] = dp[start_id + 1][target_sum - arr[start_id - 1]] + dp[start_id + 1][target_sum] 
        return
    else:
      return

  def countSubsets(self, num, sum1):
    #return self.helper(0, sum1, 0, num) # [1, 1, 2, 3], 4 => 3
    dp = [[-1 for _ in range(sum1 + 1)] for _ in range(len(num) + 1)]
    self.helper2(1, sum1, num, dp)
    return dp[1][sum1]
