# You are given a string s and an integer k. Your task is to remove groups of identical, consecutive characters from the string such that each group has exactly k characters. The removal of groups should continue until it's no longer possible to make any more removals. The result should be the final version of the string after all possible removals have been made.
class Solution:
    def checkAndRemoveGroup(self, stack, k):
        for i in range(k):
            if stack[-i] == stack[-i+1]:
                continue
            else:
                return stack# no group found, leave stack as-is
        # a group of repeating letters is found
        return stack[:-k] # remove top k elements

    def removeDuplicates(self, s: str, k: int) -> str:
         stack = []
         for letter in s:
            stack.append(letter)
            if len(stack) >= k and stack[-1] == stack[-2]:
                stack = self.checkAndRemoveGroup(stack, k)

         return "".join(stack);
