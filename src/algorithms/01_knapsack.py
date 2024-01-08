# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
class Solution:
  
  def helper(self, index, profits, weights, capacity):
    if index == len(weights) or capacity <= 0:
      return 0
    include_profit = 0.0
    if weights[index] <= capacity:
      include_profit = profits[index] + self.helper(index + 1, profits, weights, capacity - weights[index])
    exclude_profit = self.helper(index + 1, profits, weights, capacity)
    return max(include_profit, exclude_profit)

  def solveKnapsack(self, profits, weights, capacity):
    index = 0
    return self.helper(index, profits, weights, capacity)
