# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
class Solution:
  
  def findTargetSubsets(self, nums, target):
    total_sum = sum([abs(num) for num in nums])
    dp = [[-1 for _ in range(2 * total_sum + 1)] for  _ in range(len(nums) + 1)]
    for start_id in range(len(nums), 0, -1):
      for rem_sum in range(2 * total_sum + 1):
        if start_id == len(nums):
          t = rem_sum - total_sum
          if abs(t) == abs(nums[start_id - 1]):
            dp[start_id][rem_sum] = 1
          else:
            dp[start_id][rem_sum] = 0
        else:
          dp[start_id][rem_sum] = dp[start_id + 1][rem_sum - nums[start_id - 1]] + dp[start_id + 1][rem_sum + nums[start_id + 1]]
    return dp[1][total_sum + target]
      
