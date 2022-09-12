# https://leetcode.com/problems/minimum-window-substring/class Solution:
class Solution:
    def advanceStartEndPtr(self, start, end, s, t_map):
        #print('keys: ', t_map.keys())
        #print('s', s[start])        
        
        while(end < len(s)):
            if s[start] not in t_map.keys():
                start += 1
                end += 1
            else:
                break
        #print('start: ', start) 
        return start, end
        
        
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t) - 1
        if len(t) > len(s):
            return ""
        t_map = collections.Counter(t) # maintains count of letters in 't'
        min_start = 0
        min_len_so_far = len(s)
        start, end = self.advanceStartEndPtr(start, end, s, t_map)
        #print('START: ', start)
        #print('End: ', end)        
        
        while(end < len(s)): # TODO: infinite loop fix it
            if collections.Counter(s[start:end]) - t_map is not None: # https://stackoverflow.com/a/52324065
                end += 1
            else:
                if min_len_so_far > end - start + 1:
                    min_len_so_far = end - start + 1
                    min_start = start
                start, end = self.advanceStartEndPtr(start, end, s, t_map)

                    
        if min_len_so_far == len(s): # no candidate substring found
            return ""
        else:
            return s[min_start:min_start + min_len_so_far]            
                    
            
                    
                    
            
                    
        
            
        
