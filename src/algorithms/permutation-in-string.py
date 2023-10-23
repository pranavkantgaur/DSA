# Given a string and a pattern, find out if the string contains any permutation of the pattern.
from collections import Counter
class Solution:
  def findPermutation(self, str1, pattern):    
    left = 0
    right = len(pattern) - 1
    pattern_freq = Counter(pattern)
    if right < len(pattern):      
      while(right < len(str1)):
        window_freq = Counter(str1[left: right + 1])
        if window_freq == pattern_freq:
          return True
        else:
          left += 1
          right += 1          
    return False
