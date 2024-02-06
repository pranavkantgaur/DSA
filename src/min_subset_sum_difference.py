# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
  def helper(self, start_id, current_sum, min_sum_so_far, arr):
    if start_id == len(arr) - 1: # base case
        include = abs(total_sum - 2 * (current_sum + arr[start_id]))
        exclude = abs(total_sum - 2 * current_sum)
        return min(min_sum_so_far, include, exclude)
        
    min_sum_so_far = self.helper(start_id + 1, current_sum + arr[start_id], min_sum_so_far, arr)
    exclude = self.helper(start_id + 1, current_sum, min_sum_so_far, arr)
    return min(min_sum_so_far, exclude)
