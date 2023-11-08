# You are given a string s and an integer k. Your task is to remove groups of identical, consecutive characters from the string such that each group has exactly k characters. The removal of groups should continue until it's no longer possible to make any more removals. The result should be the final version of the string after all possible removals have been made.
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        maintain a stack of hashmaps each hasmap contains letter and its count of successive occurance
        for each new letter if it matches the top, update the countr and if it reaches k, remove the elements.
        '''
        stack = []
        for letter in s:
            if len(stack) and letter == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([letter, 1])
            if stack[-1][1] == k:
                stack.pop(-1)
        
        result = ""
        while(len(stack)):
            letter, count = stack.pop(-1)
            for i in range(count):
                result = letter + result
        return result

