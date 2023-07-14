# https://leetcode.com/problems/minimum-window-substring/class Solution:
class Solution:             
    def get_first_matching_letter(self, s[start:], t_map):
        while(letter is not in t_map):
            start += 1
        return start            

    def substring_matches_counter(self, substring, counter):
        return Counter(substring) - counter == 0
    
    def update_min_substring(self, start, end, min_start, min_length):
        if end - start < min_length: 
            return start, end - start 
        else: 
            return min_start, min_length
    
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = len(t)
        if len(t) > len(s):
          return ""        
        if len(s) == 1 and len(t) == 1:
          if s[0] == t[0]:
            return s[0]
          else:
            return ""                                      
                
        t_map = collections.Counter(t) # maintains count of letters in 't'
        min_start = 0
        min_end = len(t)                        
        start = self.get_first_matching_letter(s[start+1:], t_map)
        end = start + len(t) - 1
        while(end < len(t)):                        
            if self.substring_matches_counter(t_map, s[start:end]):
                min_start, min_end = self.update_min_substring(min_start, min_end, start, end)    
                start = self.get_first_matching_letter(start, s, t_map)
                end = start + len(t) - 1                    
                c_map = self.update_c_map(c_map, s[start])
            else:
                end += 1                
        else:
            pass # just return the current solution
        return s[min_start:min_end]                        
            
                    
                            
            
                    
                    
            
                    
        
            
        
