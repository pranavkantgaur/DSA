# Given a non-negative integer represented as a string num and an integer k, delete k digits from num to obtain the smallest possible integer. Return this minimum possible integer as a string.
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
          while(len(stack) and k > 0 and digit < stack[-1]):
            stack.pop(-1)
            k -= 1
          stack.append(digit)
        if k > 0:
          stack = stack[:-k]
        result = "".join(stack)
        while(result):
          if result[0] == '0':
            result = result[1:]
          else:
            break
        if len(result) == 0:
          return "0"
        else:
          return result       
