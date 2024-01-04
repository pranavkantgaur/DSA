# Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects.

# We can start an investment project only when we have the required capital. After selecting a project, we can assume that its profit has become our capital, and that we have also received our capital back.

from heapq import *

class Solution:
  def findMaximumCapital(self, capital, profits, numberOfProjects, initialCapital):
    min_heap, max_heap = [], [] # max_heap maintain a priority queue of all projects in our budget at any time.
    # push all proj. to min_heap based on capital required
    total_num_of_projs = len(profits)
    for i in range(total_num_of_projs):
      heappush(min_heap, (capital[i], [capital[i], profits[i]]))
    # until number of investments < num_of_projs, continue investing:
    invest_ctr = 0
    av_capital = initialCapital 
    while(invest_ctr < numberOfProjects): 
      while(len(min_heap) and min_heap[0][0] <= av_capital): 
        heappush(max_heap, -heappop(min_heap)[1][1]) # add all project in our budget to the max_heap
      if len(max_heap):        
        av_capital += -heappop(max_heap) # invest
        invest_ctr += 1
      else: # not possible to invest further.
        break
    return av_capital  
