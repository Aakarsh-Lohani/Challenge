#https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/
"""
2976. Minimum Cost to Convert String I
Medium

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
 

Constraints:

1 <= source.length == target.length <= 10^5
source, target consist of lowercase English letters.
1 <= cost.length == original.length == changed.length <= 2000
original[i], changed[i] are lowercase English letters.
1 <= cost[i] <= 10^6
original[i] != changed[i]
"""
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def build(original, changed, costs):
            graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
            for ori, ch, cost in zip(original, changed, costs):
                graph[ori][ch] = min(graph[ori][ch], cost)
            return graph
        
        def dijkstra(graph, start_node, target_node):
            if start_node not in graph:
                return float('inf')
            
            visited_nodes = set()
            min_heap = [(0, start_node)]

            while min_heap:
                cost_to_current, current_node = heapq.heappop(min_heap)
                if current_node == target_node:
                    return cost_to_current
                if current_node in visited_nodes:
                    continue
                visited_nodes.add(current_node)
                for neighbor_node in graph[current_node]:
                    if neighbor_node not in visited_nodes:
                        heapq.heappush(min_heap, (cost_to_current + graph[current_node][neighbor_node], neighbor_node))
            return float('inf')
        
        graph = build(original, changed, cost)
        total_cost = 0
        memo = {}

        for s, t in zip(source, target):
            if s != t:
                if (s, t) in memo:
                    cost = memo[(s, t)]
                else:
                    cost = dijkstra(graph, s, t)
                    memo[(s, t)] = cost
                if cost == float('inf'):
                    return -1
                total_cost += cost

        return total_cost
            
            
