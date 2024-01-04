# Given an array of intervals, find the next interval of each interval. In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

# Write a function to return an array containing indices of the next interval of each input interval. If there is no next interval of a given interval, return -1. It is given that none of the intervals have the same start point.

from heapq import *


#class Interval:
#  def __init__(self, start, end):
#    self.start = start
#    self.end = end


class Solution:
  def findNextInterval(self, intervals):
    n = len(intervals)
    result = [-1 for x in range(n)]
    maxend_heap, maxstart_heap = [], []
    for id, interval in enumerate(intervals):
      heappush(maxend_heap, (-interval.end, [id, interval]))
      heappush(maxstart_heap, (-interval.start, [id, interval]))
    while(len(maxend_heap)):
      while(len(maxstart_heap) and -maxstart_heap[0][1][1].start >= maxend_heap[0][1][1].end):
        _, [start_id, _] = heappop(maxstart_heap)
        result[maxend_heap[0][1][0]] = start_id
      heappop(maxend_heap)
    return result
