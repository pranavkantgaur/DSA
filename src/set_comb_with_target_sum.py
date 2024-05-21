# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
class Solution:
  def helper(self, start_id, A, abs_sum, num, dp):
    if start_id <= len(num) and A >= 0  and A < 2 * abs_sum: # valid state
      if dp[start_id][A] != -1: return
      elif start_id == len(num):
        target_sum = A - abs_sum
        if abs(target_sum) == abs(num[start_id - 1]):
          dp[start_id][A] = 1
        else:
          dp[start_id][A] = 0
      else:                            
        dp[start_id][A] = 0 
        if A - num[start_id - 1] >= 0:
          self.helper(start_id + 1, A - num[start_id - 1], abs_sum, num, dp) 
          dp[start_id][A] = dp[start_id + 1][A - num[start_id - 1]]
        if A + num[start_id - 1] <= 2 * abs_sum:
          self.helper(start_id + 1, A + num[start_id - 1], abs_sum, num, dp)        
          dp[start_id][A] += dp[start_id + 1][A + num[start_id - 1]]
  
  def findTargetSubsets(self, num, s):
    abs_sum = 0
    for number in num:
      abs_sum += abs(number)
    dp = [[-1 for _ in range(2 * abs_sum + 1)] for _ in range(len(num) + 1)]
    self.helper(1, s + abs_sum, abs_sum, num, dp)
    return dp[1][s + abs_sum]
