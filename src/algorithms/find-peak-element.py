'''
https://leetcode.com/problems/find-peak-element/
Input: nums = [1,2,3,1]
Output: 2

1. Questions:
   1. wht abt. first and last numbers?
   2. elements distinct?
   3. sorted?
   4. if length = 1, return -1
   5. No solution: what to return? all increasing or decreasing array, return -1
2.1 B.F. approach: (O(n))
   1. Slideing window: Compare each element with its left and right neighbors:
      1.1. Set left = -inf, right = arr[1], right = inf for index = n - 1
      1.2. return the first peak
2.2 Optimized:
    2.2.1. Bindary search based

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        for id, num in enumerate(nums):
            if not id:
                if num > nums[id + 1]:
                    return id
                else:
                    continue
            if id == len(nums) - 1:
                if num > nums[id - 1]:
                    return id
                else:
                    continue
            first = nums[id - 1]
            last = nums[id + 1]                
            if num > first and num > last:
                return id
            else:
                continue
        
