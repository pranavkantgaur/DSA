# https://leetcode.com/problems/word-search-ii
'''
1. Construct a trie for the input list of words
2. For each cell in the board, traverse the trie and search for leaves:
   * If a leaf is found during board visit, add that string to the result
   * Else, continue
3. If DFS is over without getting matching strings in the trie, return None

-------
How to build a Trie?
C: Create trie:
I/P: ["aab", "aca", "aabbc", "acbcd", "dfres", "gre", "great"]
O/P:                 root
             a           d       g
          a     c          f       r
        b*      a*           r       e
                         e             a 
                        s*              t*
                        
R: Read/check if a word exists in the trie?
* I/P: ["aab", "aca", "aabbc", "acbcd", "dfres", "gre", "great"], word = "grea"/"aa"/"res"
* O/P: False/False/False
U: Add a new string to trie? Update an exisiting string?
D: Remove a string from trie?
  * Starting from the leaf node matching the last letter of deleted string:
    * Move up and delete all nodes which only have one descendant, untill we reach the root.
    * If a parent with more than 1 descendant is found, STOP.
-------
How to use Trie and DFS to get list of words which exist over the board?
'''
