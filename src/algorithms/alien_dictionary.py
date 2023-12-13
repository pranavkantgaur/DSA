# There is a dictionary containing words from an alien language for which we don’t know the ordering of the letters. Write a method to find the correct order of the letters in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its letters.

class Solution:  
  def get_unique_letters(self, words):
    unique_letters = list(set(list(''.join(words))))
    return unique_letters

  def update_graph(self, pre_word, dep_word, graph, indeg): # ba, bc
    i1, i2 = 0, 0
    while(i1 < len(pre_word) and i2 < len(dep_word)): # i1 < 2, i2 < 2
      if pre_word[i1] == dep_word[i2]:                        
        i1 += 1
        i2 += 1
      else:
        if dep_word[i2] not in graph[pre_word[i1]]:             
          graph[pre_word[i1]].add(dep_word[i2])
          indeg[dep_word[i2]] += 1
        return # only once, because following letters cannot be compared using these 2 word pairs. # graph: [a->c, b->a,c]

  def get_topological_order(self, graph, indeg):
    sources = [i for i in indeg.keys() if indeg[i] == 0] # [b]
    sorted_order = []
    while(len(sources)):
      source = sources.pop(0)
      sorted_order.append(source) # [bac]
      for dep in graph[source]:
        indeg[dep] -= 1
        if indeg[dep] == 0:
          sources.append(dep) # [c]
    return ''.join(sorted_order)


  def findOrder(self, words):
    letters = self.get_unique_letters(words) # 3
    # init graph
    graph = {letter:set() for letter in letters} # {a:{}, b:{}, c:{}}
    indeg = {letter:0 for letter in letters} # {a:0, b:0, c:0}

    # build graph
    for p_id in range(len(words)):
      for d_id in range(p_id + 1, len(words)):
        self.update_graph(words[p_id], words[d_id], graph, indeg) # (ac, cab, graph, indeg)
    # return topological traversal
    return self.get_topological_order(graph, indeg)
    
