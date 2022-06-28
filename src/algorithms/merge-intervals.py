# https://leetcode.com/problems/merge-intervals/
class Solution:
    
    def mergeUtil(self, index, intervals):
        new_interval = [intervals[index][0], intervals[index + 1][1]]
        intervals.pop(index)
        intervals.pop(index)
        intervals.insert(index, new_interval)
        return
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for index in range(len(intervals)):
            if index + 1 <= len(intervals) - 1:
                if intervals[index][1] >= intervals[index][0]:
                    self.mergeUtil(index, intervals)
                else:
                    continue
        return intervals                    
            
        