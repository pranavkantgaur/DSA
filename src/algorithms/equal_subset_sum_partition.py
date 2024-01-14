# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
class Solution:
  
  '''
  How to create a dp array for this? what is the state of the problem?
  start id, length of subarray, 
  '''

  def findKSubset(self, arr, start_id, k, curr_sum, total_sum, dp):
    if curr_sum == total_sum - curr_sum: 
      dp[start_id][k] = 1
      return True
    if start_id == len(arr) or len(arr) - start_id < k: 
      dp[start_id][k] = 0
      return False
    if dp[start_id + 1][k - 1] == -1:
      self.findKSubset(arr, start_id + 1, k - 1, curr_sum + arr[start_id], total_sum, dp)
    include = dp[start_id + 1][k - 1]
    if not include:
      if dp[start_id + 1][k] == -1:
        self.findKSubset(arr, start_id + 1, k, curr_sum, total_sum, dp)
    exclude = dp[start_id + 1][k]
    return include or exclude

  def canPartition(self, arr):
    total_sum = sum(arr)
    dp = [[[-1] for _ in range(len(arr) + 1)] for _ in range(len(arr) + 1)]
    for k in range(1, len(arr) // 2 + 1):
      for start_id in range(len(arr) - k + 1):
        curr_sum = 0
        if self.findKSubset(arr, start_id, k, curr_sum, total_sum, dp): return True # given the subarray starting from start_id, find if we have a subset of size k for which 2 subset equality is satisfied?
    return False
