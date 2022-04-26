# https://www.pramp.com/challenge/wqNo9joKG6IJm67B6z34
'''
BF: 
1. Sanity checks: 
   1. If len of str < len of arr: return ""
2. initial window size  = len of arr
3. while(window size < len str):
     found, result = checkForMatchingSubstring(str, ws):
     if found:
       return result
     increase windows size
4. if not found
   return " "

Optimize:
1. s = 0, e =  0 #len(arr) - 1
2. init hashmap of arr with 1 representing visied and 0 representing not visited
3. if h[str[e]] == 0: # element pointed to by e is present in arr and is not visired yet in curret substring search
      #mark as visited
      h[str[e]] = 1
      visited_counter += 1
      if visited_counter == len(arr):
        if e - s + 1 == len(arr):
          return str[s: e]
        else:
          found, s_small, e_small = getSmallestSubtring(s, e)
          if found and e_small - s_small == len(arr):
            return arr[s_small: e_small]
          elif not found:            
            # update min
            # try to create a minimal string from this s:e, update s and e?
            if min_len > e - s + 1:
              min_len = e - s + 1
              res_s = s
              #res_e = e
            s += 1    
    e+=1       
   return str[res_s:res_s + min_len]
      
#str: xxxxxyz
'''
def get_shortest_unique_substring(arr, str):
  pass # your code goes here

#input:  arr = ['x','y','z'], str = "xyyzyzyx"
