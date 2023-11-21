# https://www.geeksforgeeks.org/problems/tic-tac-toe2412/1
#User function Template for python3

class Solution:
    def isValid(self, board):
        # code here
        # check if n_x - n_o != 1, return false
        
        def get_count(board, letter):
            count = 0
            for cell in board: 
                if cell == letter: count += 1
            return count
            
        def check_winner(board, letter):
            # check rows
            win_pattern = [letter, letter, letter]
            if win_pattern  == board[0:3] or win_pattern  == board[3:6] or win_pattern  == board[6:9]: return True
            # check colms
            if win_pattern  == [board[0], board[3], board[6]] or win_pattern  == [board[1], board[4], board[7]] or win_pattern  == [board[2], board[5], board[8]]: return True
            # check diagona
            if win_pattern  == [board[0], board[4], board[8]] or win_pattern  == [board[2], board[4], board[6]]: return True
            return False
            
        n_o = get_count(board, 'O')
        n_x = 9 - n_o
        if n_x - n_o != 1: return False
        else: 
            if check_winner(board, 'O'): return False
        if check_winner(board,'O') and check_winner(board,'X'): return False
        
        return True
        # check if os along
'''
X X O
O O X 
O X X
'''
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        board = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.isValid(board)
        if ans:
            print("Valid")
        else:
            print("Invalid")
        tc -= 1

# } Driver Code Ends
