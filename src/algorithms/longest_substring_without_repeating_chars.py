# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Clarify:
1. Solution always exist?
2. Expected TC/SC?
3. Case sensitive?


Test-case:
1. s = aaaaa, o->1
2. s=abababa, o->2
3. s=abcderf, o->7
4. s=+-abc , o->4

Naive algoritm: TC->O(n^2), SC->O(1)
1. For each substring,
   1, Check if it contains unique letters
   2. If yes, update max_length
2. Return max_length   

Better, using hashmap and growing window: TC: O(n), SC: O(n)
1. start with a smallest window defined by start and end pointers:
   1. Compute counter_map
   2. Update max_len
   3, Grow window by adding the current letter to the hmap and incremeneting the end pointer.
   4. TODO
'''
