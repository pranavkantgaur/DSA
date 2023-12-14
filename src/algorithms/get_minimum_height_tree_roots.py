# We are given an undirected graph that has the characteristics of a k-ary tree. In such a graph, we can choose any node as the root to make a k-ary tree. The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). There can be multiple MHTs for a graph. In this problem, we need to find all those roots which give us MHTs. Write a method to find all MHTs of the given graph and return a list of their roots.

from collections import deque

class Solution:
  def findTrees(self, nodes, edges):
    graph = {i:[] for i in range(nodes)}
    indeg = {i:0 for i in range(nodes)}
    for edge in edges:
      graph[edge[0]].append(edge[1])
      graph[edge[1]].append(edge[0])
      indeg[edge[0]] += 1
      indeg[edge[1]] += 1
    sources = [i for i in range(nodes) if indeg[i] == 1] # add leaf nodes
    while(len(indeg) >= 3):
      level_size = len(sources)
      for _ in range(level_size):
        source = sources.pop(0)
        for dep in graph[source]:
          indeg[dep] -= 1 
          graph[dep].remove(source)       
          if indeg[dep] == 1:
            sources.append(dep)
        del indeg[source]
        del graph[source] # shrink the graph
    return list(indeg.keys())
