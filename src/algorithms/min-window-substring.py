# https://leetcode.com/problems/minimum-window-substring/
import sys

class Solution:                 
    def minWindow(self, s: str, t: str) -> str:                                                      

        t_map = collections.Counter(t) # maintains count of letters in 't'
        
        # initialize start to point to first matching letter
        start = 0
        while(start <= len(s) - 1 and s[start] not in t_map):
            start += 1        
        # set end to minimum viable value
        end = start + len(t) 
        
        # track the solution
        min_start = 0
        min_end = sys.maxsize # set to an invalid window size

        # track candidates
        c_map = None
        if end <= len(s):
            c_map = Counter(s[start:end])

        # search for solution among candidates
        while(end <= len(s)):                                                            
            if (t_map - c_map) == Counter():
                if min_end - min_start > end - start:
                    min_start, min_end = start, end                                  
                c_map[s[start]] -= 1
                start += 1                
                while(start <= len(s) - 1 and s[start] not in t_map):
                    c_map[s[start]] -= 1 # update the counter map to reflect the sliding of substring window.
                    start += 1
            else:                
                if end < len(s):
                    c_map[s[end]] += 1
                end += 1                  
                    
        # if no candidate was found        
        if min_end == sys.maxsize:
            return ""                
        else:
            return s[min_start: min_end]    
