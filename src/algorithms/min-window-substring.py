# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t) - 1
        if len(t) > len(s):
            return ""
        t_map = collections.Counter(t) # maintains count of letters in 't'
        # fix start
        while(end < len(s)):
            if s[start] is not in t_map:
                start += 1
                end += 1
        # update end
        while(end < len(s)):
            if s[start:end] != t_map:
                end += 1
            else:
                if min_len_so_far > end - start + 1:
                    min_len_so_far = end - start + 1
                    min_start = start
                    end += 1
                    # TODO, go to first while loop
                else:
                    end += 1
                    
                
        return s[min_start:min_start + min_length_so_far]            
            
                    
        
            
        
