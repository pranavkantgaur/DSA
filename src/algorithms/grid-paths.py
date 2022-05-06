'''
# https://www.interviewbit.com/problems/grid-paths/

1. Clarify:
   Given a grid, find cost of all paths from (0, 0) to (N-1, N-1)
     * Path does not have cycles
     * Path has all unblocked nodes of the grid only once.
   
  Input 1:

  A : 
  [
    [5, 2]
    [0, 7]
  ]
  Output 1:

  8

  A : 
  [
    [79, 19, 59]
    [45, 89, 63]
    [79, 81, 37]
  ]


2. Min 2 approach
   BF:
   * At A[0, 0] -> 2 directions, visit all non zero nodes(as subproblems), if any point, path becomes invalid, leave the path/backtrack
     * for each neighbor of node: while(queue):
       * if neighbor is N-1, N-1: updateTotalPathSum(current_path), return
       * if neighbor is not 0:
           current_cost += abs(neighbor.value - node.value)
           queue.push(neighbor)
        elif neighbor.val = 0:
            return           
3. Code
4. TC, SC, Edge cases
'''
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
