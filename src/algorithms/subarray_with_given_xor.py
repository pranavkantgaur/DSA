'''
# https://www.interviewbit.com/problems/subarray-with-given-xor/
Clarify:
1. Solution for all inputs exists? what to return?
2. what is bitwise XOR, xoring bits of all elements of a subarray position-wise?
3. Array is sorted?
4. What is the expected TC, SC?

Test caseS:
1. [12, 45, 67, 21, 1], 9 -> convert all numbers to binary representation

Naive approach: TC: O(n^2), if bitwise XOR is O(n) then TC-> O(n^3), SC-> O(1)
1. Get binary representation for all input numbers
2. For each possible subaray compute bitwise xor
3. If the xor is = target number: increment count, else continue
4. return count

Is there a property of numbers with repect to the target bitwise XOR value?
'''
