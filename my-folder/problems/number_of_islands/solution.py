class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count=0
        rows=len(grid)
        columns=len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]=="1":
                    count=count+1
                    self.Dfs(grid,i,j)
                        
        return count
    
    def Dfs(self,grid,i,j):
        rows=len(grid)
        columns=len(grid[0])
        
        if i<0 or j<0 or i>=rows or j>=columns or grid[i][j]!="1":
            return 0
        grid[i][j]=0
        
        self.Dfs(grid,i-1,j)
        self.Dfs(grid,i+1,j)
        self.Dfs(grid,i,j+1)
        self.Dfs(grid,i,j-1)
        
        