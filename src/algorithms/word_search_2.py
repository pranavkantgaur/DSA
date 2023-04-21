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

class Solution:   
    def is_neighbor_valid(self, neighbor, x_lim, y_lim):
        if neighbor[0] >= 0 and neighbor[0] < x_lim and neighbor[1] >= 0 and neighbor[1] < y_lim:
            return True
        else:
            return False            
    def helper(self, board: List[List[str]], start_x: int, start_y: int, words_trie_node: TrieNode, current_string: str, result: Set[str], visited: List[bool][bool]):
        if words_trie_node[board[start_x][start_y]] is not None:
            current_string.append(board[start_x][start_y])
            visited[start_x][start_y] = True
            if words_trie_node.is_leaf == True:
              result.insert(current_string)
            else:
              #continue
              pass
            words_trie_node = words_trie[board[start_x][start_y]]
            neighbors = [[start_x + 1, start_y], [start_x, start_y + 1], [start_x - 1, start_y], [start_x, start_y - 1]]
            for neighbor in neighbors:
                if is_valid_neighbor(neighbor) and visited[neighbor[0]][neighbor[1]] == False:
                  self.helper(board, neighbor_x, neighbor_y, words_trie[board[][]], result)
                else:
                  continue
            visited[start_x][start_y] = False                
        else:
            return                
        return          

    '''
    Trie must support: constructor, get_dummy_root(), stores hashmaps of size 26(alphabets) for each node 
    '''    
    Class Trie():
        def __init__(self):
	        self.dummy_root = TrieNode()
	
        def insert(self, string):
	        for letter in string:
		        if self.trie_node[letter] is not None:
			        trie_node = trie_node[letter]
		        else:
			        new_trie_node = TrieNode()
			    trie_node[letter] = new_trie_node
		        #If it is last letter of the string:
                    #Trie_node[letter].is_leaf = True
                # else:
	                #continue

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()        
        visited = [[] for i in range(len(board))]
        for row in visited:
            row = [False for i in range(len(board[0]))]
        words_trie = TrieNode()
        for word in words:
            words_trie.insert(word)
        current_string = ""
        for row in board:
            for col in board:
                self.helper(board, board_x, board_y, words_trie.get_dummy_root(), curent_string, result, visited)
        return list(result)        
