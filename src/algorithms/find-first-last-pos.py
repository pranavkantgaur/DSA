'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
BF: 
0. Check if arr[0] <= target <= arr[n - 1]: if true then continue else return [-1, -1]
1. Linearly search for the element from left to right
2. Mark the first position where the element is found as start
3. Continue untill current element is different from target value, set last index as current - 1, mark as last
4. return start, last index

TC: O(n)
SC: O(1)

Binary search:
-1. if arr is None: return [-1, -1]
0. Check if arr[0] <= target <= arr[n - 1]: if true then continue else return [-1, -1] # sanity check
1. Locate the element in the array, say index i = bsearch(low, high, target) else return [-1, -1] # within range but not in array
2. Check if a[i - 1] == target, if true: k = bsearch(low, i - 1, target), else, set start = i # fix start with binary searches
   2.-1. if i == 0: start = i, and skip 2.x
   2.0. k = i
   2.1. while(a[k - 1] == target):
          high = k - 1
          if high == 0:
            start = 0
            break
          else:
            k = bsearch(low, high, target)
   2.2. start = k       
3. Check if a[i + 1] == target, if true: m = bsearch(i + 1, high, target), end = m, else, set end = i # fix end with binary searches
   3.-1. if i == len(a) - 1: end = i, skip 3.x
   3.0. k = i
   3.1. while(a[k + 1] == target):
          low = k + 1
          if low == len(a) - 1:
            end = low
            break
          else:  
            k = bsearch(low, high, target)
   3.2. end = k       
4. return [start , end]
'''

class Solution:
    def bsearch(self, low, high, target, nums):
        while(low <= high):
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1    
            
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:  # sanity checks
            return [-1, -1]
        if nums[0] == nums[-1]: # sanity check, if all elements are identical
            if nums[0] == target:
                return [0, len(nums) - 1]
            else:
                return [-1, -1]
        low = 0
        high = len(nums) - 1
        i = self.bsearch(low, high, target, nums)
        if i == -1: # sanity check
            return [-1, -1]
        else:
            start = -1
            end = -1
            # locate the start
            if i == 0:
                start = i
            else:
                k = i
                is_bsearch_not_required = False
                while(nums[k - 1] == target):
                    high = k - 1
                    if high == 0:
                        is_bsearch_not_required = True
                        break
                    k = self.bsearch(low, high, target, nums)                        
                    
                if is_bsearch_not_required:
                    start = 0
                else:
                    start = k
            # locate the end
            if i == len(nums) - 1:
                end = i
            else:
                k = i
                is_bsearch_not_required = False
                #low = 0
                high = len(nums) - 1 # reinit since it may have been overwritten by start finding bsearches.
                while(nums[k + 1] == target):
                    low = k + 1
                    if low == len(nums) - 1:
                        is_bsearch_not_required = True
                        break
                    k = self.bsearch(low, high, target, nums)   
                if is_bsearch_not_required:
                    end = low
                else:
                    end = k  
            
            return [start, end]        
