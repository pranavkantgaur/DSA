# https://leetcode.com/problems/permutations/'''
'''
Approach 1:
1. For each number in the nums list:
   1.1. Set that number as the first number of the permutation and permute remaining numbers
        1.1.1 Recursively do this untill the nums size is 2 when you can return with [nums[0], nums[1]] and [nums[1], nums[0]]

2. Striver: https://youtu.be/YK78FU5Ffjw
   2.1. Backtrack: maintain a stack of numbers in the current permutation and a 'flags' array of numbers positions of 
        which are taken 
   2.2. If len of stack == len nums: add stack to result and remove top from stack and unflag for corresponding element.
   2.3. For each number in nums:
        add num to stack and mark flag
        
        


'''
class Solution:
    '''
    results = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [[nums[0]]]
        if len(nums) == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        else:
            for num in nums:         
                next_nums = nums.copy()
                next_nums.remove(num)
                #print("Next nums: ", next_nums, nums)
                permutation_result = self.permute(next_nums) # since numbers are distinct
                #print('RESULT: ', permutation_result)
                for result in permutation_result:                                        
                    result.insert(0, num)
                    self.results.append(result)    
            return self.results                
       '''
    def backtrack(self, nums_length, nums, stack, result):
            if len(stack) == nums_length:
                #print('NUMS', nums_length, stack)
                result.append(stack)
                #print('RRULKTD', result)
                # prep for backtrack
                print('Before: ', stack)
                stack.pop() 
                print('After: ', stack)
                return # backtrack
            else:
                for num in nums:
                    print('1: ', stack)                    
                    stack.append(num)
                    print('2: ', stack)
                    new_nums = nums.copy()
                    new_nums.remove(num)
                    print('Neew new: ', stack, new_nums)
                    #print('Renmi ved: ', num)
                    #print('from: ', nums)
                    #print('gives: ', new_nums)
                    #if new_nums == [2]:
                    #    print("CHeck!!", stack)
                    self.backtrack(nums_length, new_nums, stack, result)
            return                    
                
    def permute(self, nums: List[int]) -> List[List[int]]:
            result = []
            stack = []            
            self.backtrack(len(nums), nums, stack, result)
            return result
            
    
