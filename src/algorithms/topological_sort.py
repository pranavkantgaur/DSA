from collections import deque

class Solution:
  def getSources(self, vertices, edges):
    sources = set()
    not_sources = set()
    for edge in edges:
      sources.add(edge[0])
      not_sources.add(edge[1]) 
    sources = sources.intersection(not_sources)
    return list(sources)

  def removeSources(self, sources, vertices, edges):
    vertices -= len(sources)
    print(vertices)
    for id, edge in enumerate(edges):
      if edge[0] in sources:
        edges.pop(id)
    return vertices, edges

  def sort(self, vertices, edges):
    result = []
    sources = []
    while(vertices > 0):
      sources = self.getSources(vertices, edges)
      result.append(sorted(sources))
      vertices, edges = self.removeSources(sources, vertices, edges)
    return result
