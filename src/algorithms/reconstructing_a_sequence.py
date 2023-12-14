# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

# Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.

from collections import deque

class Solution:
  def canConstruct(self, originalSeq, sequences):
    '''
    # create a graph
    # do topological traversal: if there are more than 1 sources at any point return false, else continue
    # if could be done then check the order if it matches originalseq, else return false
    '''
    # init graph
    unique_nums = {e for seq in sequences for e in seq}
    graph = {i:set() for i in unique_nums}
    indeg = {i:0 for i in unique_nums}
    # build graph
    for seq in sequences:
      for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
          if seq[j] not in graph[seq[i]]:
            graph[seq[i]].add(seq[j])
            indeg[seq[j]] += 1
    # build topo order
    sources = [i for i in unique_nums if indeg[i] == 0]
    order = []
    while(len(sources)):
      if len(sources) > 1: 
        return False
      source = sources.pop(0)
      order.append(source)
      for dep in graph[source]:
        indeg[dep] -= 1
        if indeg[dep] == 0:
          sources.append(dep)
    return order == originalSeq
