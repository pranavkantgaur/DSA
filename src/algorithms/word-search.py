# https://leetcode.com/problems/word-search/
class Solution:
    def helper(board, word, letter_index, start_pos):
        if letter_index == len(word):
            return True
        if word[letter_index] != board[start_pos[0]][start_pos[1]]:
            return False
        else:
            visited[start_pos[0]][start_pos[1]] = True            
            neighbors = [[start_pos[0] - 1, start_pos[1]], [start_pos[0], start_pos[1] - 1], [start_pos[0], start_pos[1] + 1], [start_pos[0] + 1, start_pos[1]]]
            for neighhbor in neighbors:
                if len(board[0]) - 1 < neighbor[1] or neighbor[1] < 0:
                    continue
                if len(board) - 1 < neighbor[0] or neighbor[0] < 0:
                    continue
                # else it is a valid neighbor
                if visited[neighbor[0]][neighbor[1]] == False:
                    if self.helper(board, word, letter_index + 1, start_pos = neighbor) == True:
                        return True
                    else:                        
                        continue
                else:
                    continue
            return False            
               
       

    def exist(board, word):
        m = len(board)
        n = len(board[0])
        if len(word) > m * n:
            return False
        i = 0
        for row in range(m):
            for col in range(n):
                if helper(board, word, i, start = [row, col]) == True:
                    return True
        return False       
    
    
 
