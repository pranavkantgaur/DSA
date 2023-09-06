# https://leetcode.com/problems/rotate-image
'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


1 2 3
4 5 6 
7 8 9

7 4 1
8 5 2
9 6 3




Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


5 1 9 11
2 4 8 10
13 3 6 7
15 14 12 16



15 13 2 5
14 3  4 1
12 6  8 9 
16 7 10 11 


Naive approach: TC -> , SC - > 
1. Identify no. of rings in the matrix to be rotated clockwise:
2. For each ring, store the content in a 1x3 buffer and overrite it with the target 1x3 values, swap the values from the buffer with the corresponding target 1x3, swap the values with target 1x3 and so on.
   * Can I go edge by edge, like storing the content of edge in a buffer and overwriting the elements at its place, then swapping the content of buffer with that on its target edge and so on? 

for 3x3 case: [2, 0] -> 0, 0, [1, 0] -> [0, 1], [0, 0] -> 0, 2, [0, 1] -> [1, 2], [0, 2] -> [2, 2], [1, 2] -> [2, 1], [2, 2] -> [2, 0], [2, 1] -> [1, 0], [] 

for 5x5 case: 
Ring 1: [3, 0] -> 0,0, [2, 0] -> [0, 1], [1, 0] -> [0, 2], [0, 0] -> [0, 3]
Ring 2: [2, 1] -> [1, 2], [1, 1] -> [2, 2]


Another approach:
1. Whether transpose followed by reversing of elements along each row = rotate by 90 deg. along clockwise?
'''
