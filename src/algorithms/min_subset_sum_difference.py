# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
class Solution:  
  def helper(self, start_id, current_sum, min_diff, arr):
    # base case, 1 element array    
    if start_id == len(arr) - 1:
      include_diff = abs(sum(arr) - 2 * (current_sum + arr[start_id]))
      exclude_diff = abs(sum(arr) - 2 * current_sum)
      return min(min_diff, include_diff, exclude_diff)
    # recursive cases
    include_diff = self.helper(start_id + 1, current_sum + arr[start_id], min_diff, arr)
    exclude_diff = self.helper(start_id + 1, current_sum, include_diff, arr)
    return exclude_diff

  def canPartition(self, num):
    return self.helper(0, 0, sum(num), num)
    
