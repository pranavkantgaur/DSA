# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.
from collections import deque

class Solution:
  def isSchedulingPossible(self, tasks, prerequisites):
    # build task prerequite graph(adjacency matrix)
    graph = {i:[] for i in range(tasks)}
    indeg = {i:0 for i in range(tasks)}
    for prerequisite in prerequisites:
      graph[prerequisite[0]].append(prerequisite[1])
      indeg[prerequisite[1]] += 1
    # identify current prerequisites for all tasks
    sources = [i for i  in range(tasks) if indeg[i] == 0]
    finished_tasks = []
    while(len(sources)):
      source = sources.pop(0) # remove a prerequisite
      finished_tasks.append(source)
      for task in graph[source]:
        indeg[task] -= 1 
        if indeg[task] == 0: # whether the dependent task is a prerequisite for all remaining tasks?
          sources.append(task)
    return len(finished_tasks) == tasks
