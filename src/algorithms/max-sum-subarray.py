# https://leetcode.com/problems/maximum-subarray/

'''
 Set start=0, end=k-1
 Compute sum of subarray (start, end)
 Update max sum
 While (end < len(array)): if end is not last element: sum -= arr(start) + arr(end)
 Check in while loop if sum is greater than the max, if yes update else continue
 At the end of while loop, return max sum
'''
