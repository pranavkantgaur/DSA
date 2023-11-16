# https://leetcode.com/problems/largest-rectangle-in-histogram/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        hMap_lr = {}
        hMap_rl = {}
        for id in range(len(heights)):
            while(len(stack) and heights[stack[-1]] > heights[id]):
                hMap_lr[stack.pop(-1)] = id
            stack.append(id)
        while(len(stack)):
            hMap_lr[stack.pop(-1)] = len(heights)

        # right to left
        for id in range(len(heights) - 1, -1, -1):
            while(len(stack) and heights[stack[-1]] > heights[id]):
                hMap_rl[stack.pop(-1)] = id
            stack.append(id)
        while(len(stack)):
            hMap_rl[stack.pop(-1)] = -1
            
        for id in range(len(heights)):
            area = heights[id] * (hMap_lr[id] - hMap_rl[id] - 1)
            if area > max_area:
                max_area = area
        return max_area
