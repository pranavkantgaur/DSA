# https://www.interviewbit.com/problems/prefix-with-key-greater-than-x/
'''
1. Clarify
   insertStringWithKey(S, K)
   getCountStringPrefixSKeyGreaterK(S, K)
   Input 1:

    A = [1, 1, 2, 1, 2]
    B = ["abc", "bac", "ab", "abc", "ab"]
    C = [5, 1, 4, 4, 4]     
   Output 1:
    [1, 2]

   insert("abc", 5), insert("bac", 1), count("ab", 4), insert("abc", 1), count("ab", 4)
   O/P:                                         1                             2


2. Min 2 appr.
   1. Representing as hash
      * insert(str, key): store string in hash table indexed by key # O(1)
      * count(str, key):
        1. Get strings with matching prefix # O(n * S), traverse hash table from key = input key onwards to get strigs, and compare prefix with str
        2. if there is a prefix match, increment the counter
        3. return counter
    2. Representing as trie:
       * insert/builds the trie: store in trie: O(S) if S is avg. size of string 
         * how to store the keys in trie of strings: store in the node corresponding to last char of a string?
       * count:  O(S)      
         * traverse the trie and once the last letter of input string is reached at node X(of trie): # O(S)
           * Do BFS/DFS on the substree rooted at X: # O(S)
             * For each node if key >= input key, update counter
         * return counter    

3. Code.          
   def insert(str, key):
       for letter in str:
            for each child of current_parent:
                if child.str = letter:
                    current_parent = child 
                else:
                    continue 
            # no child matched
            child = Node(letter)
            current_parent.child.append(child)
            current_parent = child
        # once entire str is parsed and represented in trie
        current_parent.key = key 
    
    def count(str, key):
        counter = 0
        # reach end of str in trie
        for each letter of str:
            for each child of current_parent:
                if child.str == letter:
                    current_parent = child
                    match_count += 1
                else:
                    continue                    
        # if string not found in any child
        if match_count != len(str):
            return 0 # no match for str as prefix
        else:            
            # do BFS and updated counter
            queue.push(current_parent)
            while(queue):
                node = queue.pop()
                if node.key >= key:
                    counter += 1
                else:
                    continue
                for each child of node:
                    queue.push(child)                                        
        return counter                    



4. TC, SC, Edge cases
'''
class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
