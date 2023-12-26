# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
from heapq import *

class Solution:
  def rearrangeString(self, str1): 
    '''
    1. create hmap
    2. in an infinite loop: take out 2 distinct most frequent letters from heap, append them to the result.
    3. if more occurances of any of them are left, push the updated count into the heap
    4. repeat untill the heap is empty.
    '''
    # create hmap
    hmap = {}
    for letter in str1:
      if letter in hmap:
          hmap[letter]+= 1
      else:
          hmap[letter] = 1 
    result = ''    
    max_heap = []
    # create max heap
    for key in hmap:
      if hmap[key] > 0:
        heappush(max_heap, (-hmap[key], key))    
    while(True):
      if len(max_heap) == 0:
        return result 
      elif len(max_heap) == 1 and -max_heap[0][0] > 1: 
        return '' # not possible        
      else:
        # take out letters and append to the result
        count1, key1 = heappop(max_heap) # max freq. letter
        count1 = -count1
        hmap[key1] -= 1
        result += key1
        if len(max_heap): # if there is another distinct letter left
          count2, key2 = heappop(max_heap)        
          count2 = -count2        
          hmap[key2] -= 1
          result += key2
          if hmap[key1]:
            heappush(max_heap, (-hmap[key1], key1))
          if hmap[key2]:
            heappush(max_heap, (-hmap[key2], key2))
        else: # if only one distinct char is left for rearrangment
          if hmap[key1]: # but we have more than 1 occurances of that, invalid
            return ''
          else: # rearrangment is complete
            return result
