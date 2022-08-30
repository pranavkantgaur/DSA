# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = 0
        # get frequency of letters in target string, t_map
        # while end does not reach the end of string:
          # update start and end untill s[start] does not belong to t_map
          # once start points to a letter contained in t_map, check if s_map[start:end] match t_map
            # if not continue updating end ptr and checking if s_map[start:end] match t_map
               # if there is a match, update min_substring so far and update start to next letter(in t_map)
               # if there is no match, continue updating end pointers 
        t_map = collections.Counter(t) # maintains count of letters in 't'
        while(end < len(s)):
            start = self._update_start()
            end = start
            if collections.Counter(s[start : end]) == t_map:
                if min_subs_len_so_far > end - start:
                    min_subs_len_so_far = end - start
                    min_start = start            
                    start = self._update_start()                            
                end += 1
                        
        return s[start:end]            
            
        
            
        
