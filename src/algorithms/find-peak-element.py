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
    class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) >> 1
        
        while(start < end):
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] > nums[mid]:
                end = mid - 1
            elif nums[mid + 1] > nums[mid]:
                start = mid + 1

'''
import math

class Solution:
    
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1       
        while(start <= end):
            if start == end:
                return start
            mid = (start + end) >> 1
            if mid > 0:
                left = nums[mid - 1]
            else:
                left =  -1.0 * math.inf
            if mid < len(nums) - 1:    
                right = nums[mid + 1]
            else:
                right = -1.0 *  math.inf
            if nums[mid] > left and nums[mid] > right:
                return mid
            elif left > nums[mid]:
                end = mid - 1
            elif right > nums[mid]:
                start = mid + 1

        
