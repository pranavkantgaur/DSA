'''
# https://www.geeksforgeeks.org/count-number-of-distinct-substring-in-a-string/
Given a string, count all distinct substrings of the given string.

Examples: 

Input : abcd
Output : abcd abc ab a bcd bc b cd c d
All Elements are Distinct

Input : aaa
Output : aaa aa a aa a a
All elements are not Distinct

Clarify:
1.Case sensitive?
2.No numbers?
3. Expected TC/SC: O(n), O(n) for n length string

Test-cases:
1. s = aaaa -> a, aa, aaa, aaaa -> 4
2. s = abcd -> abcd, abc, ab, a, bcd, bc, b, cd, c, d -> 10
3. s = abab-> abab, aba, ab, a, bab, ba, b -> 7
4. s = abcddd -> abcddd, abcdd, abcd, abc, ab, a, bcddd, bcdd, bcd, bc, b, cddd, cdd, cd, c, ddd, dd, d -> 18
5. ?


Approach using conditioned-Trie(conditioned on the string s): TC: O(), SC: O()
1. Create the trie and increment the counter for each trie leaf: 
   1. From root node, take out nodes with each possible substring starting letter from the string s, :
      1. Create child node for all letters of the string:
         1. Node will have [letter, remaining_string] as its id. So that even if the letter is same, remaining_string will differentiate the sibling-nodes at any level.
   2. repeat the process for all nodes, 
   3. if we hit a leaf, increment the counter    
2. Return the counter

Bottlenecks:
0. Whther this approach is REALLY going to generate ALL substrings?
1. Whether the trie approach is TC O(n)? No, 
2. Is there a different representation of substrings using trie than the one i am discussing above?

'''
