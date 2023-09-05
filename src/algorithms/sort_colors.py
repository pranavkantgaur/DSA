# https://leetcode.com/problems/sort-colors/
'''
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]



Algo 1: TC -> O(n), SC -> 0(1)
1. Compute count of 0,1, 2 in one pass
2. Update the array as per count and 0-1-2 order in second pass.


def sortColors(nums):
  # 1st pass
  hMap = {}
  for num in nums:
    hMap[num] += 1
  # 2nd pass
  i = 0
  for num in range(3):
    while(hMap[num] > 0):
      nums[i] = num
      hMap[num] -= 1 		    
      i += 1

* But this is not sorting as-such, it just emulates sorting by directly overwriting the content of result array, guided by hash-map.

Algo2: Single pass SC->O(1), TC->O(n):
* What are the bottleneck in above algo? Why not do it in single pass?
  * If I get a 2, swap it with the last element which is not 2.
  * If I get a 1, swap it with last element which is less than 1
  * If I get a 0, continue. 
'''
