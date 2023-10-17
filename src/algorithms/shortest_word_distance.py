# Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
class Solution:
  def shortestDistance(self, words, word1, word2):
    ptr1 = -1
    ptr2 = -1
    current = 0
    min_distance = len(words)
    while(current < len(words)):
      if words[current] in [word1, word2]:
        if ptr1 == -1:
          ptr1 = current
        else:
          if words[current] == words[ptr1]:
            ptr1 = current
            if ptr2 != -1:
              if min_distance > ptr1 - ptr2:
                min_distance = ptr1 - ptr2
              ptr2 = -1                            
          else:
            ptr2 = current
            if min_distance > ptr2 - ptr1:
              min_distance = ptr2 - ptr1    
      current += 1                      
    return min_distance

