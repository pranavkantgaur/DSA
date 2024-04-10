# You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.
class Solution:
  def helper(self, start_id, target_sum, num):
    if start_id == len(num):
      if target_sum - num[start_id - 1] == 0 or target_sum + num[start_id - 1] == 0:
        return 1
      else:
        return 0
    return self.helper(start_id + 1, target_sum - num[start_id - 1], num) + self.helper(start_id + 1, target_sum + num[start_id - 1], num) 
  def findTargetSubsets(self, num, s):
    return self.helper(1, s, num)
