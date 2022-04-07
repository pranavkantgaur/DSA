# https://www.geeksforgeeks.org/find-next-greater-number-set-digits/
'''
Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Not Possible"

Input: n = "534976"
Output: "536479"

Approach:
1. Vist from right letter to left letter
   1.1. If a[i - 1] > a[i]: continue
   1.2. else: search k such that i+1 <= k <= n - 1 and 
        a[k] > a[i - 1] and a[k] < a[j] where i + 1 <= j <= n - 1
        swap a[k], a[i - 1]
        sort a[i:n - 1]       
        return a
   1.3. return False        
'''
def findNextBiggestDigit(a, startID, endID, arr):
  '''
   finds next biggest number wrt a in arr between startID and endID
  ''''
  
def findGreaterNum(number : str):
  for (i = n - 1; i >= 1; i--):
    if a[i - 1] > a[i]: 
      continue
    else:
      # find k
      k = findNextBiggestDigit(a[i - 1], i+1, n-1, a) # could be based on linear search or heap
      # swap a[i - 1], a[k]
      t = a[k]
      a[k] = a[i]
      a[i] = t    
      # sort a[i:n]
      a[i:n] = a[i:n].sort()
      # return a
      return a
  return False    
'''
TC: O(n)
SC:
'''
   
