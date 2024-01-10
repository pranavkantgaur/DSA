# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
class Solution:
  def solveKnapsack(self, profits, weights, capacity):
    if len(weights) == 0 or capacity == 0:
      return 0
    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]        
    for index in range(len(weights), 0, -1):
      for cap in range(capacity + 1):
        if index == len(weights): # last position in input array, decision-making is purely based on the direct comparison between current capacity and last item weight
          if cap >= weights[index - 1]:
            dp[index][cap] = profits[index - 1]
          else:
            dp[index][cap] = 0
        else:        
          include_profit = 0
          if cap >= weights[index - 1]:
            include_profit = profits[index - 1] + dp[index + 1][cap - weights[index - 1]]             
          exclude_profit = dp[index + 1][cap]
          dp[index][cap] = max(include_profit, exclude_profit)
    return dp[1][capacity]    
