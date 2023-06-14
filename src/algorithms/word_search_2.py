class TrieNode(object):
    def __init__(self):
        self.alpha_map = dict.fromkeys(string.ascii_lowercase, None) 
        self.alpha_map['#'] = None # to avoid visiting same cell on the board multiple times during a string match
        self.is_leaf = False
        self.word = None

class Trie(object):
    def __init__(self):
        self.trie_root = TrieNode()
        self.number_of_words = 0

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
        current_node.word = word # add this word to trienode      
        self.number_of_words += 1  
        
        

class Solution:   
    def helper(self, board: List[List[str]], start_row: int, start_col: int, trie_obj: Trie, words_trie_node: TrieNode, result: List[str]) -> None:                
        if start_row < 0 or start_row > len(board) - 1 or start_col < 0 or start_col > len(board[0]) - 1:
            return
        if words_trie_node.alpha_map[board[start_row][start_col]] is not None and trie_obj.number_of_words > 0: # compare letter on the board with trie           
            if words_trie_node.alpha_map[board[start_row][start_col]].is_leaf == True:
              leaf_node = words_trie_node.alpha_map[board[start_row][start_col]]
              result.append(leaf_node.word) 
              words_trie_node.alpha_map[board[start_row][start_col]].is_leaf = False # avoids duplicate strings             
              trie_obj.number_of_words -= 1 
            else:              
              pass

            words_trie_node = words_trie_node.alpha_map[board[start_row][start_col]]
            t = board[start_row][start_col]            
            board[start_row][start_col] = '#' # here I am editing the key so that it is not found.
            self.helper(board, start_row, start_col + 1, trie_obj, words_trie_node, result)
            self.helper(board, start_row, start_col - 1, trie_obj, words_trie_node, result)
            self.helper(board, start_row + 1, start_col, trie_obj, words_trie_node, result)
            self.helper(board, start_row - 1, start_col, trie_obj, words_trie_node, result)
            board[start_row][start_col] = t                       
        else:
            return                
        return          
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []        
        words_trie = Trie()
        n_rows = len(board)
        n_cols = len(board[0])
        board_size = n_rows * n_cols
        for word in words:
            if len(word) <= board_size:
                words_trie.insert(word)
            else:
                continue                        
        for row in range(n_rows):
            for col in range(n_cols):
                self.helper(board, row, col, words_trie, words_trie.trie_root, result)
        return result       
