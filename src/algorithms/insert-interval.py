# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for index, interval in enumerate(intervals):
            if self.isOveralapping(newInterval, interval):
                newInterval = self.mergeInterval(newInterval, interval) # update newInterval
                new_interval_index = index # mark the index
                intervals.pop(index) # remove the interval
            else:
                continue # look for overlap
        if new_interval_index is not None:
            intervals.push(new_interval_index, newInterval)                
        else: # newInterval did not overlap with input intervals
            # it should be added to either of the ends of intervals
            if intervals[0][0] > newIntervals[1]:
                intervals.insert(0, newInterval)
            else:
                intervals.insert(len(intervals) - 1, newInterval)
            
        return intervals
