# https://leetcode.com/problems/insert-interval/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1. Binary search both start_new and end_new of newInterval in intervals to get indices i and j
        2. Remove all intervals from intervals list between indices i and j(including i, j)
        3. Insert new Interval as [min(start_i, start_new), max(end_j, end_new)]
        4. Return intervals
        '''
