# https://leetcode.com/problems/unique-paths/
'''
Test cases:
1. m,n = 3, 3, o/p -> 6


*1, 1, 1
1, 1, 1
1, 1, 1*

2. m, n = 1, 1, o/p -> 1
3. m, n = 2, 1, o/p->1
4. m, n = 3, 4, o/p = 
*1, 1, 1, 1
1, 1, 1, 1
1, 1, 1, 1*

5. m, n = 4, 3, o/p =     
    
Naive algorithm: TC-> O(2^(n  + m))
1. Start from top-left corner
2. path_count = Simulate going to right, sub-divide the problem with right side mopmvement considered as the starting position, 
3. path_count += Simulate going down, sub-divide the problem with down movement considered as the starting position
4. Return path_count, sol = f(sol(n, m - 1), sol(n - 1, m)) => T(n, m) = T(n, m-1) + T(n-1, m)


# without memoization
def numUniquePaths(grid):
  m = len(grid)	
  n = len(grid[1])
  if m = 0 or n = 0:
    return 1	
  else:
    seed = 0, 0  
    count = numUniquePaths(grid[1:,])	
    count += numUniquePaths(grid[, 1:])
    return count


With memoization: Using the solution:
1.
'''
        
