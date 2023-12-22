# Given an array of points in a 2D plane, find ‘K’ closest points to the origin.

from heapq import *


#class Point:

#  def __init__(self, x, y):
#    self.x = x
#    self.y = y

  # used for max-heap
#  def __lt__(self, other):
#    return self.distance_from_origin() > other.distance_from_origin()

#  def distance_from_origin(self):
    # ignoring sqrt to calculate the distance
#    return (self.x * self.x) + (self.y * self.y)

class Solution:
  def findClosestPoints(self, points, k):
    if len(points) < k: return []
    max_heap = []
    for point in points:
        #print(point)
        if len(max_heap) < k:
            heappush(max_heap, point)
        else:
            if point > max_heap[0]: # max_heap[0] is the kth farthest point
                heappop(max_heap)
                heappush(max_heap, point)
            else:
              print(point, max_heap[0])                
    result = []
    while(len(max_heap)):
        result.append(heappop(max_heap))
    return result[::-1]
