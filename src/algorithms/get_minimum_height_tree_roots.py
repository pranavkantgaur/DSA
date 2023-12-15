# https://leetcode.com/problems/minimum-height-trees/
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i : [] for i in range(n)}
        indeg = {i:0 for i in range(n)}

        # build graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            indeg[edge[0]] += 1
            indeg[edge[1]] += 1
        sources = [i for i in range(n) if indeg[i] == 1]

        while(len(indeg) >= 3):
            level_size = len(sources) # leaves at current level
            for _ in range(level_size):
                source = sources.pop(0)
                for dep in graph[source]:
                    indeg[dep] -= 1
                    graph[dep].remove(source)
                    if indeg[dep] == 1:
                        sources.append(dep)
                del graph[source]
                del indeg[source]
        return list(indeg.keys())

        
