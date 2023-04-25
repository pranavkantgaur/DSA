# https://leetcode.com/problems/implement-trie-prefix-tree/
import string 

class Node:
    def __init__(self):
        self.alpha_node_map = {}
        self.is_leaf = False
        self.alpha_node_map = dict.fromkeys(string.ascii_lowercase, None)

    def get_alpha_node_map(self):
        return self.alpha_node_map

class Trie:
    def __init__(self):
        self.trie_root = Node()

    def insert(self, word: str) -> None:
        next_node = self.trie_root    # TODO cleanup node iteration    
        for letter in word:            
            if next_node.get_alpha_map()[letter] is not None:
                next_node = next_node[letter]
            else:
                next_node_map[letter] = Node()
                next_node_map = next_node_map[letter]
        next_node.is_leaf = True

    def search(self, word: str) -> bool:
        next_node_map = self.trie_root.get_alpha_node_map()
        for letter_id, letter in enumerate(word):
            if next_node[letter] is not None:
                next_node = next_node[letter]
                if next_node.is_leaf is True:
                    #if letter is last:
                    if letter_id == len(word) - 1: # last letter of the word
                        return True
                    else:
                        continue                                
                else:
                    continue                        
            else:
                return False
        return False # case when no match was found                         
        

    def startsWith(self, prefix: str) -> bool:
        '''
        Returns true if there is a previously inserted string which has same prefix.
        '''
        next_node = self.trie_root.get_alpha_node_map()
        for letter in word:
            if next_node[letter] is not None:
                next_node = next_node[letter]
            else:
                return False
        return True                                
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
