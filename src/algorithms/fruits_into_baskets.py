# https://leetcode.com/problems/fruit-into-baskets/description/
import math

class Solution:
  def findLength(self, fruits):
      max_length = 0
      start = 0
      hMap = {}
      for end in range(len(fruits)):
        if fruits[end] in hMap.keys():
          hMap[fruits[end]] += 1
        else:
          hMap[fruits[end]] = 1
        while(len(hMap.keys()) > 2):
          hMap[fruits[start]] -= 1
          if hMap[fruits[start]] == 0:
            del hMap[fruits[start]]
          start += 1          
        max_length = max(max_length, end - start + 1)
      
      return max_length
