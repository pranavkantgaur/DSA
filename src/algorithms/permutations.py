# https://leetcode.com/problems/permutations/
'''
Approach 1:
1. For each number in the nums list:
   1.1. Set that number as the first number of the permutation and permute remaining numbers
        1.1.1 Recursively do this untill the nums size is 2 when you can return with [nums[0], nums[1]] and [nums[1], nums[0]]
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
