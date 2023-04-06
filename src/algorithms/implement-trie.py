# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:
    class Node:
        def __init__(self):
            self.alpha_node_map = {}
            for letters in englist_alphabet:
                self.alpha_node_map[letter] = None


    def __init__(self):
        self.trie_root = Node

    def insert(self, word: str) -> None:
        next_node = self.tree_root
        for letter in word:            
            if letter in next_node.keys():
                next_node = next_node[letter]
            else:
                next_node[letter] = Node()
                next_node = next_node[letter]
        next_node.is_leaf = True

    def search(self, word: str) -> bool:
        next_node = self.trie_root
        for letter in word:
            if letter in next_node.keys():
                next_node = next_node[letter]
                if next_node.is_leaf is True:
                    if letter is last:
                        return True
                    else:
                        return False
                else:
                    continue                                
            else:
                return False
        return False # case when no match was found                         
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
