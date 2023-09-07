'''
# https://leetcode.com/problems/merge-sorted-array/

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.



[1, 2, 2, 3, 5, 6]


Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

[1]


Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

[1]

Conmstrait: O(m + n)

Naive algorithm: TC -> O(m + n), SC: O(m + n)
1. Set two ptrs 1 for nums1, another for nums2
2. In a loop, compare the values pointed to by num1ptr and num2ptr until num1ptr or num2ptr does not reach the end.
   1. Put the smallest of the values into the aux array
   2. Advance the ptr pointing to the smaller value in respective array
   
Approach 2: TC: O(mlogn ??), SC->O(m + n)
For each element in num1, do binary search in num2, if element is found, put all preceding numbers in num2 into the aux array, and then place the searched number into the aux array, repeat the process for next element in num1, untill we reach the end of num1, post that simply copy the remaining elements of num2, if any


   
Algoritm with SC -> O(1)   

'''
