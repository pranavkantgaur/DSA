# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:  
    def search(self, nums: List[int], target: int) -> int:        
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = left + (right - left) // 2 
            if nums[mid] == target: 
                return mid
            else:
                if nums[mid] > nums[left]: # left-mid part is sorted,
                    id = self.search(nums[left: mid], target)
                    if id != -1:
                        return left + id
                    else:
                        left = mid + 1
                else:
                    # mid + 1 to right is sorted.
                    id = self.search(nums[mid + 1: right], target)
                    if id != -1:
                        return mid + id  
                    else:
                        right = mid - 1
        if nums[left] == target: 
            return left
        else:
            return -1        
