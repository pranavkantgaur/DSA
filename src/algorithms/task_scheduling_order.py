# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.
from collections import deque

class Solution:
  def findOrder(self, tasks, prerequisites):
    sortedOrder = []
    graph = {i: [] for i in range(tasks)}
    indeg = {i: 0 for i in range(tasks)}

    for prerequisite in prerequisites:
      graph[prerequisite[0]].append(prerequisite[1])
      indeg[prerequisite[1]] += 1
    
    sources = [i for i in range(tasks) if indeg[i] == 0]

    while(len(sources)):
      source = sources.pop(0)
      sortedOrder.append(source)
      for prerequisite in graph[source]:
        indeg[prerequisite] -= 1
        if indeg[prerequisite] == 0:
          sources.append(prerequisite)
    
    if len(sortedOrder) != tasks: return []
    
    return sortedOrder
