# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.
from collections import deque

class Solution:
  def __init__(self):
    self.orders = []


  def print_topo_orders(self, graph, indeg, sources, sortedOrder):
    if len(sources):
      for source in sources:
        sortedOrder.append(source)
        sources_downtream = sources.copy()
        sources_downtream.remove(source)        
        for dep in graph[source]:
          indeg[dep] -= 1
          if indeg[dep] == 0:
            sources_downtream.append(dep)
        self.print_topo_orders(graph, indeg, sources_downtream, sortedOrder)        
        for dep in graph[source]:
          indeg[dep] += 1
        sortedOrder.pop(-1)
        
    else:
      if len(sortedOrder) == len(indeg):
        self.orders.append(sortedOrder.copy())
        print(sortedOrder)
        print('res: ', self.orders)
        
  
  def printOrders(self, tasks, prerequisites):
    if tasks == 0:
      return []
    # subdivide using recursion when multiple sources are detected in current graph
    graph = {i: [] for i in range(tasks)}
    indeg = {i:0 for i in range(tasks)}
    for prerequisite in prerequisites:
      graph[prerequisite[0]].append(prerequisite[1])
      indeg[prerequisite[1]] += 1
    sources = [i for i in range(tasks) if indeg[i] == 0]
    sortedOrder = []
    self.print_topo_orders(graph, indeg, sources, sortedOrder)
    #print('check: ', self.orders)
    return self.orders
