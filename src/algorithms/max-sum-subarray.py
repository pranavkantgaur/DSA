# https://leetcode.com/problems/maximum-subarray/
'''
Iterative:
1. if all elements of the array are +ve, return sum of array elements
2. If all elements are -ve, return the min element
3. Create islands of =ve nuymbers, merge +ve subarray as a single number:
   --- + ---- + -- + (+ is a single number after merging +ve numbers, - is a -ve number)
4. Merging +----+ if sum is greater than max(+, +)  

Recursive:
1. return max(num + maxSubArray(nums - num), maxSubArray())
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return sum(nums) if all num in nums > 0
        return min(nums) if all num in nums < 0
        for index, num in enumerate(nums):
            if num > 0:
                start = index
            if num < 0:
                end = index
                sum_element = sum(nums[start:end])
                nums.remove(start:end)                
                nums.add(start, sum_element)
        for num in nums:
            if num < 0:
                continue
            else:
                if start is not None:
                    end = index    
                    if sum(nums[start:end] > max(nums[start], nums[end])):
                        sum_element = sum(nums[start:end])
                        nums.remove(start:end)
                        nums.add(start, sum_element)
                    start = index                        
                else:
                    start = index
                    
                
        
