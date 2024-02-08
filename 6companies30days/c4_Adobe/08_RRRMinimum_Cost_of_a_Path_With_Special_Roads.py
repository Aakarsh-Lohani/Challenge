#https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/description/
"""
2662. Minimum Cost of a Path With Special Roads
Medium

You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

 

Example 1:

Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.
Example 2:

Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.
 

Constraints:

start.length == target.length == 2
1 <= startX <= targetX <= 10^5
1 <= startY <= targetY <= 10^5
1 <= specialRoads.length <= 200
specialRoads[i].length == 5
startX <= x1i, x2i <= targetX
startY <= y1i, y2i <= targetY
1 <= costi <= 10^5
"""
from typing import List
from heapq import heappush, heappop
class Solution:
    def minimumCost(self,start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        points = {tuple(start), tuple(target)}
        for x1, y1, x2, y2, cost in specialRoads:
            points.add((x1, y1))
            points.add((x2, y2))
        
        points = list(points)
        point_to_idx = {point: idx for idx, point in enumerate(points)}

        N = len(points)
        dis = [[float('inf')] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dis[i][j] = dis[j][i] = cost
        
        for x1, y1, x2, y2, cost in specialRoads:
            idx1, idx2 = point_to_idx[(x1, y1)], point_to_idx[(x2, y2)]
            dis[idx1][idx2] = dis[idx2][idx1] = min(cost, dis[idx1][idx2])

        frontier = [(0, point_to_idx[tuple(start)])]
        visited = [False] * N
        
        while frontier:
            cost, node_idx = heappop(frontier)
            if visited[node_idx]:
                continue
                
            visited[node_idx] = True
            if points[node_idx] == tuple(target):
                return cost

            for next_node_idx in range(N):
                if visited[next_node_idx] or dis[node_idx][next_node_idx] == float('inf'):
                    continue
                
                heappush(frontier, (cost + dis[node_idx][next_node_idx], next_node_idx))

        return -1