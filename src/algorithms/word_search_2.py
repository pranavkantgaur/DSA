class TrieNode(object):
    def __init__(self):
        self.alpha_map = dict.fromkeys(string.ascii_lowercase, None)               
        self.is_leaf = False

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
        self.number_of_words += 1

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
    def is_valid_neighbor(self, neighbor, row_lim, col_lim):
        if neighbor[0] >= 0 and neighbor[0] < row_lim and neighbor[1] >= 0 and neighbor[1] < col_lim:
            return True
        else:
            return False   

    def helper(self, board: List[List[str]], start_row: int, start_col: int, trie_obj: Trie, words_trie_node: TrieNode, current_string: str, result: Set[str], visited: List[List[bool]]) -> None:                
        if words_trie_node.alpha_map[board[start_row][start_col]] is not None and trie_obj.number_of_words > 0: # compare letter on the board with trie
            current_string += board[start_row][start_col]            
            visited[start_row][start_col] = True
            if words_trie_node.alpha_map[board[start_row][start_col]].is_leaf == True:
              result.add(current_string) # avoids duplicate strings 
              words_trie_node.alpha_map[board[start_row][start_col]].is_leaf = False
              trie_obj.number_of_words -= 1
            else:              
              pass
            words_trie_node = words_trie_node.alpha_map[board[start_row][start_col]]
            neighbors = [[start_row + 1, start_col], [start_row, start_col + 1], [start_row - 1, start_col], [start_row, start_col - 1]]
            for neighbor in neighbors:
                if self.is_valid_neighbor(neighbor, len(board), len(board[0])) and visited[neighbor[0]][neighbor[1]] == False:
                  self.helper(board, neighbor[0], neighbor[1], trie_obj, words_trie_node, current_string, result, visited)
                else:
                  continue
            visited[start_row][start_col] = False                
        else:
            return                
        return          
    def _get_unique_letters(self, input_strings):
        unique_letter_set = set()
        for input_string in input_strings:            
                if len(unique_letter_set) < 26:
                    for letter in input_string:
                        if len(unique_letter_set) < 26:
                            unique_letter_set.add(letter)
                        else:
                            break                                    
                else:
                    break                            
        return unique_letter_set


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()        
        visited = [[] for i in range(len(board))]
        for row in range(len(visited)):
            visited[row] = [False for i in range(len(board[0]))]
        words_trie = Trie()
        n_rows = len(board)
        n_cols = len(board[0])
        board_size = n_rows * n_cols
        # get unique letters across the board        
        #board_unique_letters = self._get_unique_letters(board)
        import time
        start = time.time()
        for word in words:
            if len(word) <= board_size:
                words_trie.insert(word)
            else:
                continue                
        end = time.time()
        print(f'Trie constructed in {end - start}s')
        current_string = ""
        start = time.time()
        for row in range(n_rows):
            for col in range(n_cols):
                self.helper(board, row, col, words_trie, words_trie.trie_root, current_string, result, visited)
        end = time.time()
        print(f'DFS done in {end - start}s')
        return list(result)        
