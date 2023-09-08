'''
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
Google docs:



You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

[1, 2, 3, 1, 4] -> [1, 5], [5, 1, 2, 4] -> [1, 3]

Naive algorithm: TC-> O(n^2), SC: O(1)
1. Search for A, search for B
   1. For each number, search for this number in rest of the array, if found set A
   2. Reduce the number for sum(1, n), reduce duplicate element only once.
   3. By the end of visit, the number which is missing will be the remainder of subtraction of numbers from the sum(1, n)
2. Return [A, B]

Bottlenecks:
* Search for A is n^2: 
  * Whether multiplying 1...n and comparising it with each number help in detecting duplicate?
  * If the duplicate number could be detected, the missing number could be identified based on the remainder of substraction of numbers from the sum(1, n)


'''
