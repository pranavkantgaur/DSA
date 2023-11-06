# Given an array of integers temperatures representing daily temperatures, your task is to calculate how many days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures):
        # use monotonically decreasing stack and store the ids of days instead of corresponding tempratures.
        next_higher_temp_day = [0 for _ in range(len(temperatures))]
        stack = []
        for id in range(len(temperatures)):
          while(len(stack) > 0  and temperatures[id] > temperatures[stack[-1]]):
            prev_day_id = stack.pop(-1)
            next_higher_temp_day[prev_day_id] = id - prev_day_id        
          stack.append(id)
        return next_higher_temp_day
