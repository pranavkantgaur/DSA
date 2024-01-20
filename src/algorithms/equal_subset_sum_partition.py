# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
class Solution:
  
  '''
  How to create a dp array for this? what is the state of the problem?
  start id, length of subarray, 
  '''

  # top-down memoization implementation.
  def helper(self, arr, start_id, current_sum, total_sum, dp):
    if dp[start_id][current_sum] != -1: return dp[start_id][current_sum]
    if total_sum == 2 * current_sum: 
      dp[start_id][current_sum] = 1
      return 1
    if start_id == len(arr):
      dp[start_id][current_sum] = 0
      return 0
    include = self.helper(arr, start_id + 1, current_sum + arr[start_id], total_sum, dp)
    exclude = self.helper(arr, start_id + 1, current_sum, total_sum, dp)
    dp[start_id][current_sum] = include or exclude
    return dp[start_id][current_sum]

  def canPartition(self, arr):
    dp = [[-1 for _ in range(sum(arr) + 1)] for _ in range(len(arr) + 1)]
    can_partition = self.helper(arr, 0, 0, sum(arr), dp)
    if can_partition: 
      return True
    else: 
      return False
