class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        height = len(grid)
        length = len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= height or j < 0 or j >= length or grid[i][j] == '0':
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(height):
            for j in range(length):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)
        
        return ans
