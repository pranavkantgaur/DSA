# https://leetcode.com/problems/word-search/
'''
Notes from: https://leetcode.com/problems/word-search/solutions/27658/accepted-very-short-java-solution-no-additional-space/?orderBy=most_votes
* Uses bit-mask to store visited map in the sign-bit of each element of the board(which is a A-Z character, hence the first bit is don't care).
  * board[x][y] ^= 256 (100000000) if (x, y) is visited.
'''

class Solution:
class Solution:
    
    
    '''
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
        or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
    '''
    
    def helper(self, board, word, letter_index, start_pos):
        if letter_index == len(word):
            return True
        if start_pos[0] > len(board) - 1 or start_pos[0] < 0 or start_pos[1] > len(board[0]) - 1 or start_pos[1] < 0 or word[letter_index] != board[start_pos[0]][start_pos[1]]: 
            return False
        if letter_index == len(word) - 1:
            return True
        else:            
            temp = board[start_pos[0]][start_pos[1]]
            board[start_pos[0]][start_pos[1]] = '#'
            neighbors = [[start_pos[0] - 1, start_pos[1]], [start_pos[0], start_pos[1] - 1], [start_pos[0], start_pos[1] + 1], [start_pos[0] + 1, start_pos[1]]]
            result = self.helper(board, word, letter_index + 1, start_pos = neighbors[0]) or self.helper(board, word, letter_index + 1, start_pos = neighbors[1]) or self.helper(board, word, letter_index + 1, start_pos = neighbors[2]) or self.helper(board, word, letter_index + 1, start_pos = neighbors[3])            
            board[start_pos[0]][start_pos[1]] = temp            
            return result
               
       

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        if len(word) > m * n:
            return False
        i = 0
        for row in range(m):
            for col in range(n):
                if self.helper(board, word, i, [row, col]) == True:
                    return True
        return False
          
