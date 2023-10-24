# Given a string and a pattern, find out if the string contains any permutation of the pattern.
from collections import Counter
class Solution:
  def findPermutation(self, str1, pattern):    
    left = 0
    right = 0
    patter_freq = {}
    for letter in pattern:
      if letter in patter_freq:
        patter_freq[letter] += 1
      else:
        patter_freq[letter] = 1
    matched = 0
    while(right < len(str1)):
      if str1[right] in patter_freq:
        patter_freq[str1[right]] -= 1 # sliding right end of window
        if patter_freq[str1[right]] == 0:
          matched += 1
          
      if matched == len(patter_freq):
        return True
      if right >= len(pattern) - 1:
        print('Left, right: ', left, right)
        if str1[left] in patter_freq:
          if patter_freq[str1[left]] == 0:
            matched -= 1
          patter_freq[str1[left]] += 1 # slide left end of the window
        left += 1
      right += 1
    return False
