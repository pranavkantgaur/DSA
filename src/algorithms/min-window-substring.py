# https://leetcode.com/problems/minimum-window-substring/class Solution:
class Solution:       
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t)
        if len(t) > len(s):
            return ""
        t_map = collections.Counter(t) # maintains count of letters in 't'
        min_start = 0
        min_len_so_far = len(s) + 1 
        
        while(end < len(s)): 
            if len(t_map - collections.Counter(s[start:end])) == 0: # https://stackoverflow.com/a/52324065
                # update min length substring
                print('Match: ', s[start:end])
                if min_len_so_far > end - start:
                    min_len_so_far = end - start
                    min_start = start        
                start += 1
            if end - start > len(t) and end + 1 == len(s):
                pass
            else:
                end += 1                  

                    
        if min_len_so_far == len(s) + 1: # no candidate substring found
            return ""
        else:
            return s[min_start:min_start + min_len_so_far]            
                    
            
                            
            
                    
                    
            
                    
        
            
        
