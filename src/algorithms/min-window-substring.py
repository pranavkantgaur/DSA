# https://leetcode.com/problems/minimum-window-substring/class Solution:
    def advanceStartEndPtr(self, start, end, s, t_map):
        print('keys: ', t_map.keys())
        while(end < len(s)):
            if s[start] is not in t_map.keys():
                start += 1
                end += 1
                        
        
        
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t) - 1
        if len(t) > len(s):
            return ""
        t_map = collections.Counter(t) # maintains count of letters in 't'
        min_start = 0
        min_length_so_far = len(s)
        while(end < len(s)):
            if s[start:end] != t_map:
                end += 1
            else:
                if min_len_so_far > end - start + 1:
                    min_len_so_far = end - start + 1
                    min_start = start
                self.advanceStartEndPtr(start, end, s, t_map)

                    
        if min_length_so_far == len(s): # no candidate substring found
            return ""
        else:
            return s[min_start:min_start + min_length_so_far]            
            
                    
            
                    
        
            
        
