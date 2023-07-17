# https://leetcode.com/problems/minimum-window-substring/class Solution:
class Solution:             
    def get_first_matching_letter(self, start, s, t_map):
        while(s[start] not in t_map):
            start += 1
        return start            

    def substring_matches_counter(self, substring, counter):        
        return bool(counter - Counter(substring))
    
    def update_min_substring(self, min_start, min_end, start, end):
        if end - start < min_end - min_start: 
            return start, end
        else: 
            return min_start, min_end
    
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
        min_end = len(s)                        
        start = self.get_first_matching_letter(start, s, t_map)
        #print('Start-1: ', start)
        end = start + len(t) #- 1
        min_substring = ""
        while(end <= len(s)):                        
            if self.substring_matches_counter(s[start:end], t_map) == False:
                #print('Matched: ', s[start:end])
                min_start, min_end = self.update_min_substring(min_start, min_end, start, end)    
                min_substring = s[min_start:min_end]
                start = self.get_first_matching_letter(start+1, s, t_map)
                end = start + len(t)
            else:
                end += 1  
                
        return min_substring                        
            
                    
                            
            
                    
                    
            
                    
        
            
        
