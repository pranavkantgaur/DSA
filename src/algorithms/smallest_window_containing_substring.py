# Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.
# slide window untill a substring containing all letters of pattern is not found, once found, shrink the substring to optimize solution, continue to search for another 
# candidate by sliding the window to the next letter occuring in the pattern.
class Solution:
  def findSubstring(self, str1, pattern):
    left = 0
    right=0
    min_len = len(str1) + 1
    min_left = -1
    while (right<= len(arr)): 
      right_letter = arr[right], 
      if right_letter in pattern_dict: 
        pattern_dict[right_letter] -= 1
        if pattern_dict[right_letter] == 0: 
          matched+= 1
      if matched==len(pattern_dict): 
        min_len = min(min_len, right - left + 1)
        min_left = left
      left_letter = arr[left]
      while(left_letter not in pattern_dict and left<= right): 
        left += 1,
        left_letter = arr[left]
      if patter_dict[left_letter] == 0: matched -= 1
        pattern _dict[left_letter] += 1
      right += 1
    if min_len == len(str1) + 1:
      return ""
    return str1[min_left: min_left + min_len]; 
