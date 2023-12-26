# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.
from heapq import *
from collections import deque

class Solution:
  def reorganizeString(self, str, k):
    result = ''
    # create letter_count
    letter_count = {}
    for letter in str:
      if letter in letter_count:
        letter_count[letter] += 1
      else:
        letter_count[letter] = 1 # l: a: 2, b:2
    # push letters from hmap to a max heap
    max_heap = []
    for key in letter_count:
      heappush(max_heap, (-letter_count[key], key)) # [a, b]
    # enter in a loop:
    while(True):
      # take out max frq. letter from heap, key1
      count1, key1 = heappop(max_heap) # k1 = a
      count1 = -count1
      # update its freq. on hmap
      letter_count[key1] -= 1 # h: a:1, b:2
      result += key1 # r = a
      if letter_count[key1] > 0: # one more occurance of key1 is left and we dont have enough spacing characters!!    
        if len(max_heap) >= k - 1: 
          keys_taken_out = {key1}
          chars_inserted_so_far_count = 0
          # enter a k-sized loop             
          while(chars_inserted_so_far_count < k - 1):
            # take out next highest freq. letter
            count2, key2 = heappop(max_heap) # k2 = b
            count2 = -count2
            # update its hmap count
            letter_count[key2] -= 1 # h: a:1, b:1
            # append it to the result
            result += key2 # r: ab
            # also: append to keys_taken_out if hmap[key] > 0 
            if letter_count[key2]:
              keys_taken_out.add(key2) # s: a, b
            chars_inserted_so_far_count += 1
          # push all removed keys to heap with updated frequency
          while(len(keys_taken_out)): # 2
            key3 = keys_taken_out.pop() # k3: b
            heappush(max_heap, (-letter_count[key3], key3)) # heap: [a, b], h: a:1, b:1
        else: # not
          return '' 
      else: 
        while(len(max_heap)): # append all the remaining letters to the result and return.
          result += heappop(max_heap)[1]
        return result # abab
