'''
# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_len = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                if max_len < count:
                    max_len = count  
                count = 0 
        if count > max_len:
            max_len = count    
        return max_len
'''
