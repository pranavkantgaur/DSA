class Solution:
    def numIslandsDFS(self, grid: List[List[str]]) -> int:
        '''
        For each 1 in grid, do DFS from that position, during DFS mark eqach visited
        cell as # and increment island counter
        '''
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
        
        
