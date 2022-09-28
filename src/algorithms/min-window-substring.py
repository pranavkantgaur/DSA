# https://leetcode.com/problems/minimum-window-substring/class Solution:
class Solution:     
        
    def substringMatchesCounter(self, substring, counter):
        return Counter(substring) - counter == 0
    
    def updateMin(self, start, end, min_start, min_length):
        if end - start < min_length: 
            return start, end - start 
        else: 
            return min_start, min_length
    
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t)
        if len(t) > len(s):
            return ""
        t_map = collections.Counter(t) # maintains count of letters in 't'
        min_start = 0
        min_len_so_far = len(s) + 1 
        
        while(!(end == len(s) and not self.substringMatchesCounter(s[start:end], t_map))):
            if end == len(s) and self.substringMatchesCounter(s[start:end], t_map):
                min_start, min_length = self.updateMin(start, end, min_start, min_length)
                if end - start > len(t):
                    start += 1
                else:
                    break                                
            if end != len(s) and not self.substringMatchesCounter(s[start:end], t_map):
                end += 1
            if end != len(s) and self.substringMatchesCounter(s[start:end], t_map):
                min_start, min_length = self.updateMin(start, end, min_start, min_length)
                start += 1
                end += 1
                    
        if min_len_so_far == len(s) + 1: # no candidate substring found
            return ""
        else:
            return s[min_start:min_start + min_len_so_far]                    
            
                            
            
                    
                    
            
                    
        
            
        
