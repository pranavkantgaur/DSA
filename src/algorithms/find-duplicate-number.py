# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        uses the input array as both input number list and a hashmap(for marking a number as visited)
        '''
        bias = max(nums) + 100
        n = len(nums)
        # detect duplicate
        for num in nums:
            if num > n: # this position has been visited.
                num_index = num - bias - 1
            else:
                num_index = num - 1
            if nums[num_index] > n: # already visited once
                duplicate = num_index + 1
                break
            else: # not visited yet
                nums[num_index] += bias # mark as visited
            
        # restore the array
        for num in nums:
            if num > n:
                num -= bias
        return duplicate 
                        
        
