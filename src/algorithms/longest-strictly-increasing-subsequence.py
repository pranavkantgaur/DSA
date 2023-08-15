'''
https://leetcode.com/problems/longest-increasing-subsequence/

1. Brute-force approach:
  1.1. For each subsequence of integer array:
       1.1.1. If it is a strictly increasing subsquence:
              1.1.1.1. Update the max subsequence length
       1.1.2. Else: continue              
2. Take or not-take approach: (TODO)   
    2.1. Given nums array:
        2.1.0. If the length of array is 1: if last_element < a[0] or last_element == None, return 1 as the solution, else: return 0 # base condition
        2.1.1. if a[0] > last_elem: 
               a = Pick next element to be part of candidate solution and recursively call for sub-problem solution: a = 1 + subprob(arr[1:], last_elem = arr[0], result), 
               b = Drop next element and recursively call for sub-problem solution: b = subprob(arr[1: ], last_elem = last_elem, result) # not updating the last elem. with arr[0]
               Select the max of a, b and return as output
               else: ??
    2.2. return result 
           

'''


class Solution:

    def helper(self, nums, max_length, last_element, current_length):
        if len(nums) == 1:
            if last_element is not None:
                if last_element < nums[0]:
                    current_length +=1
                    if current_length > max_length:
                        max_length = current_length
                    return
                else:
                    return 
            else:
                max_length=1
                return
        else:
            if last_element != None:
                if last_element < nums[0]:
                    # take and not-take
                    if max_length < current_length + 1:
                        max_length = current_length + 1 
                    self.helper(nums[1:], max_length, last_element=nums[0], current_length = current_length+1) # take
                    self.helper(nums[1:], max_length, last_element, current_length) # not take
                    return
                else:
                    # look for a candidate number 
                    for idx, num in enumerate(nums):
                        if num > last_element:
                            break
                        else:
                            continue
                    if idx == len(nums) - 1:
                        max_length += 1
                        return
                    else:
                        # take and not-take
                        if max_length < current_length + 1:
                            max_length = current_length + 1 
                        self.helper(nums[idx + 1:], max_length, last_element=nums[idx], current_length = current_length+1) # take
                        self.helper(nums[idx + 1:], max_length, last_element, current_length) # not take
                        return					
            else:
                        # take and not-take
                        if max_length < current_length + 1:
                            max_length = current_length + 1 
                        self.helper(nums[1:], max_length, last_element=nums[0], current_length = current_length+1) # take
                        self.helper(nums[1:], max_length, last_element, current_length) # not take
                        return					
                
    def lengthOfLIS(self, nums: List[int]) -> int:
        last_element = None
        current_length = 0
        max_length = 0
        self.helper(nums, max_length, last_element, current_length)
        return max_length


