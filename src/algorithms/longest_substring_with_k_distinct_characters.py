# Given a string, find the length of the longest substring in it with no more than K distinct characters.
class Solution:
  def findLength(self, str1, k):
      max_length = 0
      start = 0
      hMap = {}
      for end in range(len(str1)):
        if str1[end] in hMap.keys():
          hMap[str1[end]] += 1 # expand
        else:
          hMap[str1[end]] = 1                  
        while(len(hMap.keys()) > k): # shrink to search next valid solution          
          hMap[str1[start]] -= 1
          if hMap[str1[start]] == 0: # very important to check
            del hMap[str1[start]]
          start += 1
        max_length = max(max_length, end - start + 1)          
      return max_length
