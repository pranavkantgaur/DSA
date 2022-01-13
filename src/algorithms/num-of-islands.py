class Solution:
    def dfs(self, row: int, col: int, grid: List[List[str]])-> None:
        grid[row][col] = '#'
        if row - 1 > 0 and grid[row - 1][col] == '1':
            self.dfs(row - 1, col, grid)
        if row + 1 < len(grid) and grid[row + 1][col] == '1':
            self.dfs(row + 1, col, grid)
        if col - 1 > 0 and grid[row][col - 1] == '1':
            self.dfs(row, col - 1, grid)
        if col + 1 < len(grid[0]) and grid[row][col + 1] == '1':
            self.dfs(row, col + 1, grid)
        return
        
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        if an element on the grid is 1, do DFS from there, mark each 1 element
        visited on the island as #/0 etc so as to avoid visiting starting DFS from there
        increment the counter by 1
        return counter
        '''
        island_counter = 0
        n_rows = len(grid)
        n_cols = len(grid[0])
        for row in range(n_rows):
            for col in range(n_cols):
                if grid[row][col] == '1':
                    self.dfs(row, col, grid)
                    island_counter += 1
                else:
                    continue
                    
        return island_counter
    
    def numIslandsNotWorking(self, grid: List[List[str]]) -> int:        
        num_islands = 0
        #island_ids = []
        m = len(grid)
        n = len(grid[0])          
        for i in range(m):
            for j in range(n):
                #if i == 2 and j == 2:
                #    print("gRID: ", grid[i][j])
                if grid[i][j] == "1":
                    if ((i > 0 and grid[i-1][j] == "1") or (j > 0 and grid[i][j - 1] == "1")):
                        continue
                    else:
                        #print("Increment at: {}, {}".format(i , j))
                        num_islands += 1
                        #island_started = True
                        #if j > 0:
                        #    if island_started and grid[i][j - 1]:
                        #        num_island -= 1
                        #        island_started = False                                
                else:
                    continue
        return num_islands               
    
    
        
        
