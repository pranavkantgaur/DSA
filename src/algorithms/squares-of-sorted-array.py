# https://leetcode.com/problems/squares-of-a-sorted-array/

'''
Approaches:
0. Square all elements, return the sorted result.
1. Check if all elements positive then simply square and return, if not binary search for abs(negative) in test of the array and place elements
2. Keep left and right pointer and place the bigger of the two in result array, regardless of the sign.
3. Inplace and O(n) solution: Can we optimize approach-2 for inplace? Best solutions(in discuss section) are also not inplace.
   
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        nums = [pow(num, 2) for num in nums]
        '''
        if nums[0] >= 0 and nums[-1] >= 0:
            return [pow(num, 2) for num in nums]
        else:
            '''
            use 2 pointer approach
            '''
            start = 0
            end = len(nums) - 1
            result = []
            while(start < end):
                if abs(nums[start]) < abs(nums[end]):
                    result.append(pow(nums[end], 2))
                    end -= 1
                elif abs(nums[start]) > abs(nums[end]):
                    result.append(pow(nums[start], 2))
                    start += 1
                else:
                    result.append(pow(nums[start], 2))
                    result.append(pow(nums[end], 2))
                    start += 1
                    end -= 1
            if start == end:
                result.append(pow(nums[start], 2))      
            #print('resutlt: ', result)        
        return reversed(result)
        
