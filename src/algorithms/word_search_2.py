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

class TrieNode(object):
    def __init__(self):
        self.alpha_map = dict.fromkeys(string.ascii_lowercase, None)               
        self.is_leaf = False

class Trie(object):
    def __init__(self):
        self.trie_root = TrieNode()

    def insert(self, word):
        if len(word) == 0:
            return
        current_node = self.trie_root
        for letter in word:
            if current_node.alpha_map[letter] is not None:
                current_node = current_node.alpha_map[letter]
            else:
                current_node.alpha_map[letter] = TrieNode()
                current_node = current_node.alpha_map[letter]
        current_node.is_leaf = True

    def print(self):
        print('Trie is: ')
        queue = []
        current_node = self.trie_root
        #print('Current node: ', current_node.alpha_map)
        while(True):                        
            for key in current_node.alpha_map.keys():
                if current_node.alpha_map[key] is not None:
                    queue.append(current_node.alpha_map[key])            
                    print(key)
                else:
                    continue        
            if len(queue) != 0:
                current_node = queue.pop(0) # take out first element of queue
                print('\n')
            else:
                break  
        

class Solution:   
    def is_valid_neighbor(self, neighbor, x_lim, y_lim):
        if neighbor[0] >= 0 and neighbor[0] < x_lim and neighbor[1] >= 0 and neighbor[1] < y_lim:
            return True
        else:
            return False   

    def helper(self, board: List[List[str]], start_x: int, start_y: int, words_trie_node: TrieNode, current_string: str, result: Set[str], visited: List[List[bool]]) -> None:                
        if words_trie_node.alpha_map[board[start_x][start_y]] is not None: # compare letter on the board with trie
            current_string += board[start_x][start_y]            
            visited[start_x][start_y] = True
            if words_trie_node.alpha_map[board[start_x][start_y]].is_leaf == True:
              result.add(current_string) # avoids duplicate strings              
            else:              
              pass
            words_trie_node = words_trie_node.alpha_map[board[start_x][start_y]]
            neighbors = [[start_x + 1, start_y], [start_x, start_y + 1], [start_x - 1, start_y], [start_x, start_y - 1]]
            for neighbor in neighbors:
                if self.is_valid_neighbor(neighbor, len(board[0]), len(board)) and visited[neighbor[0]][neighbor[1]] == False:
                  self.helper(board, neighbor[0], neighbor[1], words_trie_node, current_string, result, visited)
                else:
                  continue
            visited[start_x][start_y] = False                
        else:
            return                
        return          

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()        
        visited = [[] for i in range(len(board))]
        for row in range(len(visited)):
            visited[row] = [False for i in range(len(board[0]))]
        words_trie = Trie()
        for word in words:
            words_trie.insert(word)
        #words_trie.print()            
        current_string = ""
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.helper(board, row, col, words_trie.trie_root, current_string, result, visited)
        return list(result)        
