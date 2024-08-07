# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
class Solution:
  
  def helper(self, start_id, rem_sum, nums, dp, total_sum):
    # state valid?
    if start_id <= len(nums):
      # state solved?      
      if dp[start_id][rem_sum] == -1:
        # trivial state?
        if start_id == len(nums):
          t = rem_sum - total_sum
          if abs(t) == abs(nums[start_id - 1]):
            dp[start_id][rem_sum] = 1
          else:
            dp[start_id][rem_sum] = 0
        else:
          # subproblems solved?
          t = rem_sum - total_sum
          # t - nums[start_id - 1] => rem_sum = 
          if rem_sum - total_sum - nums[start_id - 1] < 0 or rem_sum + nums[start_id - 1] > 2 * total_sum:
            print("Error")
          if dp[start_id + 1][rem_sum - nums[start_id - 1]] == -1:
            self.helper(start_id + 1, rem_sum - nums[start_id - 1], nums, dp, total_sum)
          if dp[start_id + 1][rem_sum + nums[start_id - 1]] == -1:
            self.helper(start_id + 1, rem_sum + nums[start_id - 1], nums, dp, total_sum)
          # solve problem
          dp[start_id][rem_sum] = dp[start_id + 1][rem_sum - nums[start_id - 1]] + dp[start_id + 1][rem_sum + nums[start_id - 1]]            

    
  def findTargetSubsets(self, nums, target):
    total_sum = sum([abs(num) for num in nums])
    dp = [[-1 for _ in range(2 * total_sum + 1)] for  _ in range(len(nums) + 1)]
    self.helper(1, total_sum + target, nums, dp, total_sum)
    return dp[1][total_sum + target]
      
