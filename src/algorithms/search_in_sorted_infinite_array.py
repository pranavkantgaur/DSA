# Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array. Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

# Since it is not possible to define an array with infinite (unknown) size, you will be provided with an interface ArrayReader to read elements of the array. ArrayReader.get(index) will return the number at index; if the array’s size is smaller than the index, it will return Integer.MAX_VALUE.

import math


#class ArrayReader:

#  def __init__(self, arr):
#    self.arr = arr

#  def get(self, index):
#    if index >= len(self.arr):
#      return math.inf
#    return self.arr[index]

class Solution:
  def searchInfiniteSortedArray(self, reader, key):
    # search for number > key
    index = 1
    last_num = reader.get(index)
    while(last_num != math.inf):
      if last_num < key:
        index *= 2 # expand range
        last_num = reader.get(index)
      else:
        break
    # value at index >= key or index is out of bound for array
    left = 0
    right = index
    while(left <= right):
      mid = left + (right - left) // 2
      if reader.get(mid) >= key:
        right = mid - 1
      else: 
        left = mid + 1

    if reader.get(left) == key:
      return left
    return -1
