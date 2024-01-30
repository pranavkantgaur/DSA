# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
class Solution: 
  def canPartition(self, arr):
    total_sum = sum(arr)
    dp = [-1 for _ in range(total_sum + 1)]
    for id in range(len(arr) , -1, -1):
      right_sum = sum(arr[id:])
      for current_sum in range(0, total_sum - right_sum + 1):
        if id == len(arr):
          if current_sum * 2 == total_sum:
            dp[current_sum] = 1
          else:
            dp[current_sum] = 0
        else:
          dp[current_sum] = dp[current_sum + arr[id]] or dp[current_sum]
    return dp[0] == 1
