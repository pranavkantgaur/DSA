# Given a string S, remove all adjacent duplicate characters recursively to generate the resultant string.
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for letter in s:
          if len(stack) and stack[-1] == letter:
            while(len(stack) and stack[-1] == letter):
              stack.pop(-1)
          else:
            stack.append(letter)
        return ''.join(stack)
