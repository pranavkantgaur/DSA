# https://www.interviewbit.com/problems/subarray-cost-sum/
'''
# https://www.techinterviewhandbook.org/coding-interview-cheatsheet/

1. Input clarification: Data: , Assumptions: , range and format
2. Discuss min. 2 approaches: TC vs SC for each approach
3. Explain while coding
4. Write compilable code in clean, modular fashion
5. Brainstorm edge-cases and add additional test-cases
   
BF:
1. For each subarray: # O(N^2): N + N-1 + N-2+ ... + 1
   1.1. Compute cost: # O(N)
   1.2. Update total cost
2. Return total cost

TC: O(N^3)
SC: O(1)

Possible optimization:
1. BUD:
   1.0. Reduce 1.1 to O(1)
   1.1. Enumerating subarray: There is overlapp in subarrays
        1.1.1. Using matrix to store sums of subarray of size n - 1:
        1.1.2. Use this matrix to compute sum of n size subarray
'''
