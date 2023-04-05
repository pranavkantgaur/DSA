# https://leetcode.com/problems/implement-trie-prefix-tree/
class Trie:

    def __init__(self):
        

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
        

    def startsWith(self, prefix: str) -> bool:
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
