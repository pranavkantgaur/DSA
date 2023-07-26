'''
https://www.geeksforgeeks.org/print-subsequences-string/
'''
def get_subsequences(s, current_subs, result):
  if len(s) == 0:
    print(current_subs)
  else:
    if len(s) == 1:
      remaining_str = ''
    else:
      remaining_str = s[1:]
    get_subsequences(remaining_str, current_subs + s[0], result) # take
    get_subsequences(remaining_str, current_subs, result) # not take   
    
# Driver code
# output is set to null before passing in
# as a parameter
output = ""
input = "abcd"
get_subsequences(input, '', output)
    
