# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
class Solution:
    
  def helper(self, index, profits, weights, capacity, dp):
    if index == len(weights) or capacity == 0:
      dp[index][capacity] = 0
    elif dp[index][capacity] == -1:
      include_profit = 0
      if weights[index] <= capacity: # do we have a valid sub-problem?
        include_profit = profits[index]
        if dp[index + 1][capacity - weights[index]] == -1:      
          include_profit += self.helper(index + 1, profits, weights, capacity - weights[index], dp)
        else:
          include_profit += dp[index + 1][capacity - weights[index]]
      if dp[index + 1][capacity] == -1: # exclude problem is already solved?
        exclude_profit = self.helper(index + 1, profits, weights, capacity, dp)
      else:
        exclude_profit = dp[index + 1][capacity]
      dp[index][capacity] = max(include_profit, exclude_profit)
    return dp[index][capacity]

  def solveKnapsack(self, profits, weights, capacity):
    index = 0
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    return self.helper(index, profits, weights, capacity, dp)
