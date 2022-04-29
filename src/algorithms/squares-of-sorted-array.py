# https://leetcode.com/problems/squares-of-a-sorted-array/

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
            result.append(pow(nums[start], 2)) # for start = end case       
            #print('resutlt: ', result)        
        return reversed(result)
        
