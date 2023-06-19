# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        1. For each element:
           1.1. Check if it exisits as a key of the hashmap:
                 1.1.1. If yes, return hmap[target - element], current_index
                 1.1.2. Else, hmap[element] = current_index                 
        2. return None # if not such pair exists        
        '''                
        hmap = {}
        for curr_id, num in enumerate(nums):
            if target - num in hmap.keys():
                return [hmap[target - num], curr_id]
            else:
                hmap[num] = curr_id                
        return None                
