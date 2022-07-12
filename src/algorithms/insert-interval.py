# https://leetcode.com/problems/insert-interval/
class Solution:
    def isOverlapping(self, interval1, interval2):
        if interval2[0] < interval1[0] and interval1[0] < interval2[1] < interval1[1]:
            return True
        if interval1[0] < interval2[0] and interval2[1] < interval1[1]:
            return True
        if interval1[0] < interval2[0] < interval[1] and interval2[1] > interval1[1]:
            return True
        if interval2[0] < interval1[0] and interval1[1] < interval2[1]:
            return True
        else:
            return False
        
    def mergeIntervals(self, interval1, interval2):
        newInterval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        return newInterval
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_interval_index = None
        for index, interval in enumerate(intervals):
            if self.isOverlapping(newInterval, interval):
                newInterval = self.mergeIntervals(newInterval, interval) # update newInterval
                new_interval_index = index # mark the index
                intervals.pop(index) # remove the interval
                break
            else:
                continue # look for overlap
        if new_interval_index is not None:
            intervals.insert(new_interval_index, newInterval)                
        else: # newInterval did not overlap with input intervals
            # it should be added to either of the ends of intervals
            if intervals[0][0] > newIntervals[1]:
                intervals.insert(0, newInterval)
            else:
                intervals.insert(len(intervals) - 1, newInterval)
            
        return intervals
