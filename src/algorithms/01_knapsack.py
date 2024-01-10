# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    if len(weights) == 0 or capacity == 0:
      return 0
    dp = [-1 for _ in range(capacity + 1)]
    for index in range(len(weights), 0, -1):
      for cap in range(capacity, 0, -1): # iterating right-to-left, so that we do not access subproblem soln for the current index during include profit calculation
        if index == len(weights):
            if weights[index - 1] <= cap:
              dp[cap] = profits[index - 1]
            else:
              dp[cap] = 0
        else:
          include_profit = 0
          if weights[index - 1] <= cap:
            include_profit = profits[index - 1] + dp[cap - weights[index - 1]]
          exclude_profit = dp[cap]
          dp[cap] = max(include_profit, exclude_profit)
    return dp[capacity]  
