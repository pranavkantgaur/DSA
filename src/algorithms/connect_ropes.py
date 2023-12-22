# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths
from heapq import *

class Solution:
  def minimumCostToConnectRopes(self, ropeLengths):
    if len(ropeLengths) < 3: return sum(ropeLengths)
    cost = 0
    heapify(ropeLengths)
    while(len(ropeLengths) >= 2):
      smallest = heappop(ropeLengths)
      second_smallest = heappop(ropeLengths)
      print(smallest, second_smallest)
      cost += smallest + second_smallest
      heappush(ropeLengths, smallest + second_smallest)
    print(len(ropeLengths))
    return cost
