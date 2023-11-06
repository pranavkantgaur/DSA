# Given an array of integers temperatures representing daily temperatures, your task is to calculate how many days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
class Solution:
    def dailyTemperatures(self, temperatures):
        # using monotonically decreasing stack and a hashmap of list
        # hashmap of list contains the relative index of next higher temprature day. Since there can be multiple days with same temprature, we use a list for each key temprature.
        mon_dec_temp_stack = []
        nge_id_hmap = {}
        for temp_id in range(len(temperatures)):
          while(len(mon_dec_temp_stack) > 0 and mon_dec_temp_stack[-1][0] < temperatures[temp_id]):
            top, id = mon_dec_temp_stack.pop(-1)
            if top not in nge_id_hmap:
              nge_id_hmap[top] = []
            nge_id_hmap[top].append(temp_id - id)
            
          mon_dec_temp_stack.append([temperatures[temp_id], temp_id])  
        while(len(mon_dec_temp_stack) > 0):
          top, id = mon_dec_temp_stack.pop(-1)
          if top not in nge_id_hmap:
            nge_id_hmap[top] = []
          nge_id_hmap[top].append(0)

        next_higher_temp_day = []
        for temp in temperatures:
          next_higher_temp_day.append(nge_id_hmap[temp].pop(0))
        
        return next_higher_temp_day
