# Given a string and a pattern, find all anagrams of the pattern in the given string.
import math

class Solution:
  def findStringAnagrams(self, str1, pattern):
    result_indices = []
    # TODO: Write your code here
    left = 0
    right = 0
    pattern_freq = {}
    for letter in pattern:
      if letter in pattern_freq:
        pattern_freq[letter] + 1
      else:
        pattern_freq[letter] = 1
    matched = 0
    while(right < len(str1)):
      right_letter = str1[right]
      if right_letter in pattern_freq:
        pattern_freq[right_letter] -= 1
        if pattern_freq[right_letter] == 0:
          matched += 1
      if matched == len(pattern_freq):
        print('check: ', str1[left: right + 1])
        print('patten: ', pattern_freq)
        result_indices.append(left)
      if right >= len(pattern) - 1:
        left_letter = str1[left]
        if left_letter in pattern_freq:
          if pattern_freq[left_letter] == 0:
            matched -= 1
          pattern_freq[left_letter] += 1
        left += 1
      right += 1
    return result_indices
