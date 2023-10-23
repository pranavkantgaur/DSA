# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
from collections import Counter

class Solution:
  def findLength(self, str1, k):
      max_length = 0
      # TODO: Write your code here
      '''
      i can do atmost k letter replacement and then it must a string with same letters
      for any substring of length l >=k, number of repetitions are atleast l - k
      calid candidate of length l will have atleast l - k occurances of a single letter
      longest substring satuisfying l - k constraint is the solution. there could be multiple candidates.
      steps:
      1. for any substring, check if most_common >= l - k:
         1. if yes, update max_length, right += 1, update hmap # explore better soln
         2. if no, how to update ptrs? do right += 1 untill either right == len or most_com >= l - k
             1. if len == right:
                1. do left += 1 untill eithe right == left or most_common >= l - k
             2. else: # anyway most_com >= l - k has reached    
      '''
      left = 0
      right = 0
      while(left <= right and right < len(str1)):
        letter_count = Counter(str1[left:right + 1])        
        _, most_comm = letter_count.most_common(1)[0]
        if most_comm >=  right - left + 1 - k:
          max_length = max(max_length, right - left + 1)          
          right += 1          
        else:          
            left += 1          

      return max_length
