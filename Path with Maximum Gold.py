class Solution:
    def getMaximumGold(self, grid):
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                return 0
            gold = grid[i][j]
            grid[i][j] = 0
            maxGold = max(dfs(i+1, j), dfs(i-1, j), dfs(i, j+1), dfs(i, j-1))
            grid[i][j] = gold
            return gold + maxGold
        m, n = len(grid), len(grid[0])
        return max(dfs(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
