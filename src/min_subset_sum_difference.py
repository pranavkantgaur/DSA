# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.
def helper(self, start_id, current_sum, min_diff, dp):
    if start_id < len(arr):
        if dp[start_id][current_sum] != -1: 
            return
        else:
            if start_id == len(arr) - 1:
                include_diff = abs(sum(arr) - 2 * current_sum + arr[start_id])
                exclude_diff = abs(sum(arr) - 2 * current_sum)
                dp[start_id][current_sum] = min(min_diff, include_diff, exclude_diff)
            else:
                if dp[start_id + 1][current_sum + arr[start_id]] == -1:
                    self.helper(start_id + 1, current_sum + arr[start_id], min_diff, dp)
                include_diff = dp[start_id + 1][current_sum + arr[start_id]]
                if dp[start_id + 1][current_sum] == -1:
                    self.helper(start_id + 1, current_sum, include_diff, dp)
                exclude_diff = dp[start_id + 1][current_sum]
                dp[start_id][current_sum] = exclude_diff
           return
    else:
        return

def main(arr):
    dp = [[-1 for _ in range(sum(arr) + 1)] for _ in range(len(arr) + 1)]
    self.helper(0, 0, sum(arr), dp)
    return dp[0][0]
