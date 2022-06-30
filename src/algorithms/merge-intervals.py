# https://leetcode.com/problems/merge-intervals/
class Solution:
    
    def mergeUtil(self, index, intervals):
        new_interval = [min(intervals[index][0],intervals[index + 1][0]) \
                        , max(intervals[index][1], intervals[index + 1][1])]
        intervals.pop(index)
        intervals.pop(index)
        intervals.insert(index, new_interval)
        return
        
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index = 0
        while(index + 1 < len(intervals)):
            if intervals[index][1] >= intervals[index + 1][0] \
            and intervals[index][0] <= intervals[index + 1][1]:
                self.mergeUtil(index, intervals)
                index -= 1            
            index += 1                
        return intervals                    
            
                         
            
        
