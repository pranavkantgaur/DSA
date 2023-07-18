# https://leetcode.com/problems/minimum-window-substring/

class Solution:                 
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
          return ""        
        if len(s) == 1 and len(t) == 1:
          if s[0] == t[0]:
            return s[0]
          else:
            return ""                                      
                
        t_map = collections.Counter(t) # maintains count of letters in 't'
        start = 0
        while(start <= len(s) - 1 and s[start] not in t_map):
            start += 1        
        min_substring = ""
               
        #print('Start-1: ', start)
        end = start + len(t) 
        
        min_start = 0
        min_end = len(s)                        
        
        c_map = None
        if end <= len(s):
            c_map = Counter(s[start:end])
        
        while(end <= len(s)):                                                            
            #print('t map: ', t_map)
            #print('cmap: ', c_map)
            #print('start:end map: ', Counter(s[start:end]))
            if (t_map - c_map) == Counter():
                #print('Matched: ', s[start:end])
                if min_end - min_start > end - start:
                    min_start, min_end = start, end
                    min_substring = s[min_start:min_end]                
                c_map[s[start]] -= 1
                start += 1                
                while(start <= len(s) - 1 and s[start] not in t_map):
                    c_map[s[start]] -= 1 # update the counter map to reflect the sliding of substring window.
                    start += 1
                while(end > start + len(t)):
                    c_map[s[end]] -= 1
                    end -= 1                
                #print('Start end: ', start, end)
            else:                
                if end < len(s):
                    c_map[s[end]] += 1
                end += 1                  
                    

                
        return min_substring                        
            
                    
                            
            
                    
                    
            
                    
        
            
        
