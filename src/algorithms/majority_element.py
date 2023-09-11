'''
# https://leetcode.com/problems/majority-element/
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

[1, 2,2,2,2,3] => 4 or more occurances of 2, yes, so ans is 2


Naive approach: TC: O(n), SC = O(n)
1. Store frquence of elements in a hashmap and if the freq > n / 2 return the key

Another: TC: O(nlogn), SC = O(1)
1. Sort the array
2. Visit array, count occurances for currently running/repeating number, if it goes > n/2 return the number


Whether, TC(0(n)) and SC: O(1) possible?
'''
