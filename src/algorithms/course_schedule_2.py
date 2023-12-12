# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = []
        # initialize graph
        graph = {i:[] for i in range(numCourses)}
        indeg = {i:0 for i in range(numCourses)}

        # build graph
        for preq in prerequisites:
            graph[preq[1]].append(preq[0])
            indeg[preq[0]] += 1
        
        # create and init sources list
        sources = [i for i in range(numCourses) if indeg[i] == 0]

        # search for course order
        while(len(sources)):
            # remove a source from graph
            source = sources.pop(0)
            course_order.append(source)
            for dep in graph[source]:
                indeg[dep] -= 1
                if indeg[dep] == 0:
                    sources.append(dep)
        if len(course_order) == numCourses:
            return course_order
        else:
            return []

        
