# https://leetcode.com/problems/maximum-subarray/
'''
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

1. Setting start and end indices to a -ve number is suboptimal
Naive approach: TC: 0(n^2), SC: 0(1)
2. We can check all subarrays starting from all +ve numbers and return the one with max. value.
3. [1,-3,4,-1,2,1] is max sum subarray starting with 1 : Sum = 4
4. Advance to 4 which is the next positive number: [4, -1, 2, 1] = 6
5. Go to 2: [2, 1] = 3
6. Go to [1] = 3
7. Go to [4] = 4
8. So, out of 5 candidates, [4, -1, 2, 1] = 6 is the max, return 6 as the output

* What are the bottlenecks in the naive algo.?
1. Is it possible to have a 0(n) 2 pointer algorithm which lets say, starts with full array and continues to shrink the subarray under consideration and finally terminates with the one with max sum?
   1. Set start and end as the left-most and rightmost positive numbers.  What is there is no +ve number? return the largest number in the array as the output.
   2. Compute the sum of max = array[start:end]
   3. Look fir a subarray which has higher sum than max:
      1. Go from positve number to another positive number for updating both start and end pointers?
         1. Why should I update start and end pointers in tandem? What if I just update start or end pointer only? Seems like I will miss some candidate subarrays?
             1. But will I not be missing candidate subarrays with tandem strategy?
'''             
