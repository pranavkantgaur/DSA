# https://leetcode.com/problems/word-search/
'''
Notes from: https://leetcode.com/problems/word-search/solutions/27658/accepted-very-short-java-solution-no-additional-space/?orderBy=most_votes
* Uses bit-mask to store visited map in the sign-bit of each element of the board(which is a A-Z character, hence the first bit is don't care).
  * board[x][y] ^= 256 (100000000) if (x, y) is visited.
  
* My usage of list for storing the starting coordinates on the board for each recursive call resulted in TLE. 
  Took me 2 months to spot that.
'''

class Solution:
    def helper(self, board, word, x, y):
        if len(word) == 0:
            return True
        if x > len(board) - 1 or x < 0 or y > len(board[0]) - 1 or y < 0 or word[0] != board[x][y]: 
            return False
        if len(word) == 1:
            return True
        else:            
            temp = board[x][y]
            board[x][y] = '#'
            result = self.helper(board, word[1:], x + 1, y) or self.helper(board, word[1:], x - 1, y) or self.helper(board, word[1:], x, y + 1) or self.helper(board, word[1:], x, y - 1)            
            board[x][y] = temp            
            return result
               
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        if len(word) > m * n:
            return False
        for row in range(m):
            for col in range(n):
                if self.helper(board, word, row, col):
                    return True
        return False
