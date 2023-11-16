# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for id in range(len(heights)):
            while(len(stack) and heights[id] < heights[stack[-1]]):
                top_id = stack.pop()
                if len(stack):
                    area = heights[top_id] * (id - stack[-1] - 1)
                else:
                    area = heights[top_id] * id
                if max_area < area:
                    max_area = area
            stack.append(id)
        while(len(stack)):            
            top_id = stack.pop()
            if len(stack):
                area = heights[top_id] * (len(heights) - stack[-1] - 1)
            else:
                area = heights[top_id] * (len(heights))
            if max_area < area:
                max_area = area
        return max_area
