'''
https://www.geeksforgeeks.org/print-subsequences-string/
'''

def get_subsequences(s, current_subs, result):
  if len(s) == 0:
    result.append(current_subs)
  else:    
    current_subs.append(s[0))
    get_subsequences(s[1:], current_subs, result)
    get_subsequences(s[2:], current_subs, result)
if __name__ == '_main_':
  s = 'abeds'
  current_subs = ''
  result = []
  get_subsequences(s, current_subs, result)
  print(f'Subsequences of {s} are: {result}')
    
