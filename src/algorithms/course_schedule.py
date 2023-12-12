# https://leetcode.com/problems/course-schedule/
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        indeg = {i:0 for i in range(numCourses)}
        
        # build the graph
        for preq in prerequisites:
            graph[preq[1]].append(preq[0])
            indeg[preq[0]] += 1
        # create a inital list of sources
        sources = [i for i in range(numCourses) if indeg[i] == 0]
        course_order = []    
        while(len(sources)):
            source = sources.pop(0)
            course_order.append(source)
            for dep in graph[source]:
                indeg[dep] -= 1
                if indeg[dep] == 0:
                    sources.append(dep)
        return len(course_order) == numCourses
