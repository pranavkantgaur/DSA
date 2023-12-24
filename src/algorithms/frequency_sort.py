# Given a string, sort it based on the decreasing frequency of its characters.
from heapq import *

class Solution:
  def sortCharacterByFrequency(self, str):
    result = ''
    heap = []
    hmap = {}
    # get freq. count per letter
    for letter in str:
      if letter in hmap:
        hmap[letter] += 1
      else:
        hmap[letter] = 1
    # push keys to the min-heap with inverted frequency(max-heap)
    for key in hmap:
      item = (-hmap[key], key)
      heappush(heap, item)
    # take out keys from priority queue and add to the resulting string
    while(len(heap)):
      _, key = heappop(heap)
      result += key*hmap[key]
    return result
