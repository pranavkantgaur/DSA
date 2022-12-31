# https://leetcode.com/problems/word-search/
class Solution:
    def exist_helper(self, board, word, seed):
        if word is None:
            return True
        starting = 0
        for row in len(board):
            for col in len(board[0]):
                if word[starting] == board[row][col]:
                    # check in all neighbors for the match
                    visited[row][col] = True
                    neighbor_list = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]
                    for neighbor in neighbor_list:                        
                        if visited[neighbor[0]][neighbor[1]] == False:
                            found = self.exist_helper(board, word[start + 1], seed = neighbor)
                            if found is True:
                                return True
                            else:
                                continue    
                        else:
                            continue
                else:
                    continue        

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.exist_helper()
