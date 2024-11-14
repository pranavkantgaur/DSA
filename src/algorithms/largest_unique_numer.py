'''
Given an array of integers, identify the highest value that appears only once in the array. If no such number exists, return -1.
'''

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        # find unique numbers --- O(n)
        unique_nums = {}
        for num in A:
            if num in unique_nums:
                unique_nums[num] = -1
            else:
                unique_nums[num] = 1
        # find largest unique number --- O(n)
        for num in unique_nums:
            if unique_nums[num] != -1  and num > maxUnique:
                maxUnique = num
        return maxUnique
