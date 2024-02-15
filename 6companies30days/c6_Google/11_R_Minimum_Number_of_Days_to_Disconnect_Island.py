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
from functools import cache
from typing import List

class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_1s = abs(sum(sum(row) for row in grid))

        @cache
        def get_rc():
            for r in range(m):
                for c in range(n):
                    if grid[r][c]:
                        yield r, c


        
        island = 1
        def is_connected():
            nonlocal island
            def count(r, c):
                if r < 0 or r>= m or c < 0 or c >= n: return 0
                if grid[r][c] != island: return 0
                grid[r][c] = -island
                total = 1
                total += count(r-1, c)
                total += count(r+1, c)
                total += count(r, c-1)
                total += count(r, c+1)
                return total
            r, c = first_rc
            if not grid[r][c]:
                r, c = second_rc
            conn = count(r, c)
            island = -island
            return conn == num_1s

        if num_1s == 0:
            return 0
        elif num_1s == 1:
            return 1
        
        
        g = get_rc()
        first_rc = next(g)
        second_rc = next(g)

        if not is_connected():
            return 0
        elif num_1s == 2:
            return 2
        

        # skip = True
        num_1s -= 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                # if skip:
                #     skip = False
                #     continue
                grid[r][c] = 0
                if not is_connected():
                    # print(f"Choke at {r}, {c}")
                    return 1
                grid[r][c] = island
                
                
        return 2

if __name__=="__main__":
    solution = Solution()
    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
    print(solution.minDays(grid)) #output should be 1
