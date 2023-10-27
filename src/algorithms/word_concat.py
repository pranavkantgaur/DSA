# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
# approach: sliding window with fixed size and hashmap for word frequency counter
class Solution:
  def findWordConcatenation(self, str1, words):
    result_indices = []
    word_length = len(words[0])
    left = 0
    right = 0
    matched = 0
    pattern_freq = {}
    for word in words:
      if word in pattern_freq:
        pattern_freq[word] += 1
      else:
        pattern_freq[word] = 1
    while(right < len(str1)):
      right_word = pattern_freq[right * word_length : (right + 1) * word_length] 
      left_word = pattern_freq[left * word_length : (left + 1) * word_length]
      if right_word in pattern_freq:
        pattern_freq[right_word] -= 1
        if pattern_freq[right_word] == 0:
          matched += 1
      if matched == len(pattern_freq):
        result_indices.append(left)
        if pattern_freq[left_word] == 0:
          matched -= 1
        pattern_freq[left_word] += 1
        left += word_length
      if right_word not in pattern_freq:
        left += word_length
      right += word_length
    return result_indices
