# https://leetcode.com/problems/insert-interval/
class Solution:
    def isOverlapping(self, interval1, interval2): # [3, 8], [8, 10]
        if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
            return False
        else:
            return True
        
    def mergeIntervals(self, interval1, interval2):
        newInterval = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
        return newInterval
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        deletion_counter = 0
        insert_index = None
        
        for index, interval in enumerate(intervals):            
            if newInterval[1] < interval[0]: # no point in continuing further as the intervals are sorted.
                if insert_index is None:
                    insert_index = index
                break
            elif self.isOverlapping(newInterval, interval):                             
                newInterval = self.mergeIntervals(newInterval, interval) # update newInterval
                if deletion_counter == 0:
                    insert_index = index
                deletion_counter += 1                    
            else:
                continue # look for overlap
        #if new_interval_index is not None:
        if deletion_counter:
            for i in range(deletion_counter):
                intervals.pop(insert_index)
            intervals.insert(insert_index, newInterval)                
        else: # newInterval did not overlap with input intervals
            # it can be anywhere actually
            # start, end or somewhere in the middle
            if insert_index is not None: # to be inserted at a specific position
                intervals.insert(insert_index, newInterval)
            elif len(intervals) == 0  or intervals[0][0] > newInterval[1]:
                intervals.insert(0, newInterval)
            else:
                intervals.append(newInterval)
            
        return intervals
