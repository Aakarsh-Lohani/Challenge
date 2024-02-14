#https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/
"""
1568. Minimum Number of Days to Disconnect Island
Hard

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1):
                return
            grid[x][y] = 0
            list(map(dfs, (x, x, x+1, x-1), (y+1, y-1, y, y)))

        def count_islands():
            cnt = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        cnt += 1
            return cnt

        if count_islands() != 1:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2

if __name__=="__main__":
    solution = Solution()
    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
    print(solution.minDays(grid)) #output should be 1
