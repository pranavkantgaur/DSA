# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.
def helper(self, arr, start_id, k, curr_sum, total_sum):
    if curr_sum == total_sum - curr_sum: return True
    if start_id == len(arr) or len(arr) - start_id < k: return False
    include = self.helper(arr, start_id + 1, k - 1, curr_sum + arr[start_id], total_sum)
    if not include:
        exclude = self.helper(arr, start_id + 1, k, curr_sum, total_sum)
    return include or exclude

def main(arr):
    total_sum = sum(arr)
    for k in range(1, len(arr) // 2):
        for start_id in range(len(arr)):
            curr_sum = 0
            if self.helper(arr, start_id, k, curr_sum, total_sum): return True # given the subarray starting from start_id, find if we have a subset of size k for which 2 subset equality is satisfied?
    return False
