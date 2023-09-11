'''
# https://leetcode.com/problems/majority-element-ii/
Example 1:

Input: nums = [3,2,3]
Output: [3]

Example 2:

Input: nums = [1]
Output: [1]

Example 3:

Input: nums = [1,2]
Output: [1,2]

[8, 8, 5,6,8, 6, 5, 5, 6], len = 9, 3 or more occurance -> output = [8, 5, 6]

[1, 1, 1, 1, 2, 3, 3, 3, 3, 8], len = 10, occ. = 4 or more, output = [1, 3]

[1, 1, 3] , len = 3 , output = > 1

[1, 3, 1], output = 1

[1,1,1], output =? 1


----

Naive solution:
1. Keep a hashmap storing the count of each element occcurance in first pass
2. Append elements with count >  n/3 to the result list
3. Return result list
TC-> O(n), SC-> O(n)

Possible to have TC = O(n) SC = O(1)?
1. Storage is the bottleneck, do I really need O(n) storage?
2. If the array is sorted, then constant storage will do but the TC will increase.
3. 2 pointer approach? Linbearyly traverse and maintain element value and its frequence count for 3 (why 3?) most repeating numbers, will it be constant space?

Approach 2: TC: O(n), SC = O(1)
1. Init constant size counter map, as there could be atmost 3 numbers which are repated more than n/3 times.
2. Update the counters with corresponding key values for an array traversal.

How to maintain this 3 sized key-value store?
1. For each element:
   * Check if the element already in the dict:
     * yes: Update counter
     * no: if ??




 

Constraints:

    1 <= nums.length <= 5 * 104
    -109 <= nums[i] <= 109

'''
