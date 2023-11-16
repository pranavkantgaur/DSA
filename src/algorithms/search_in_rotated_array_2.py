# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
class Solution:
    def search(self, nums: List[int], target: int) -> bool:        
        left = 0
        right = len(nums) - 1
        while(left < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            else:
                if nums[left] <= nums[mid]: # left-mid is sorted
                    if nums[left] <= target < nums[mid]:
                        if self.search(nums[left:mid], target):
                            return True
                    left = mid + 1
                if nums[left] > nums[mid]: # mid - right is sorted
                    if nums[right] >= target > nums[mid]:
                        if self.search(nums[mid + 1: right + 1]):
                            return True
                    right = mid - 1
        return nums[left] == target
