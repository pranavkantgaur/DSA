#User function Template for python3
# https://gitlab.com/pranav/my-sprints/-/snippets/2215721
'''
Input:
a = 5, b = 5, x = 11, # dest = (5, 5), x = 11
Output:
0
      |
    - R -
      | 
      
 (-1) * x1 + 1 * x2 = a
  (-1) * y1 + 1 * y2 = b
  
  x1 + x2 + y1 + y2 = x
 
 TC: O(1)
 SC: O(1)
  ---
  Exponential TC algorithm: O(1 + 4 + 4^2 + ... + 4^x), SC: O(4^x)
  1. Start from 0, 0
  2. For each direction posibility: 
     2.1. Do BFS
     2.2. If we touch a,b at any leaf node(after x moves), return 1 else return 0
     to_visit.push([0, 0])
     step = 0
     while(step < x):
       queue_len = len(to_visit) # number of nodes at this level to be visited
       id = 0
       while(id < queue_len):
         start = to_visit.pop(0)
         next_1 = [start[0], start[1] + 1]
         next_2 = [start[0], start[1] - 1]
         next_3 = [start[0] + 1, start[1]]
         next_4 = [start[0] - 1, start[1]]
         to_visit.push(next_1)
         to_visit.push(next_2)
         to_visit.push(next_3)
         to_visit.push(next_4)
         id += 1
       step += 1
     while to_visit:
        element = to_visit.pop()
        if (element[0] == a and element[1] == b):
           return 1
        else:
            continue
     return 0            
  ---
 (a + b) mod x == 0
  
  --- 
  try solving this in 1D: given x units, and 0 starting point, each movement is +1  or -1
  given (a, x) return true or false: if a % 2 == 0 and x > a, check x % a  == 0, return true else false
  if a % 2 == 1 and x > a, check x % a == 1 return true
'''

class Solution:
    def canReach(self, a, b, x):
        to_visit = []
        to_visit.append([0, 0])
        step = 0
        while(step < x):
            queue_len = len(to_visit) # number of nodes at this level to be visited
            id = 0
            while(id < queue_len):
                start = to_visit.pop(0)
                next_1 = [start[0], start[1] + 1]
                next_2 = [start[0], start[1] - 1]
                next_3 = [start[0] + 1, start[1]]
                next_4 = [start[0] - 1, start[1]]
                to_visit.append(next_1)
                to_visit.append(next_2)
                to_visit.append(next_3)
                to_visit.append(next_4)
                id += 1
            step += 1
        while to_visit:
            element = to_visit.pop()
            if (element[0] == a and element[1] == b):
                return 1
            else:
                continue
        return 0 
        
    def canReachNaive(self, a, b, x):
        # code here
        if a == 0 and b == 0:
            if x % 2 == 0:
                return 1
            else:
                return 0
        elif a == 0:
            if b % 2 == 0 and x > b and x % b == 0: # [0, 11], x = 13
                return 1
            elif b % 2 == 1 and x > b and x % b == 1:
                return 1
            else:
                return 0
        elif b == 0:
            if a % 2 == 0 and x > a and x % a == 0:
                return 1
            elif b % 2 == 1 and x > b and x % b == 1:
                return 1
            else:
                return 0                
        if abs(a + b) != x:
            return 0
        else:
            return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,x=map(int,input().split())
        
        ob = Solution()
        print(ob.canReach(a,b,x))
# } Driver Code Ends
