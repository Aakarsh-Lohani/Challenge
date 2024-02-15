#https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/description/
"""
1617. Count Subtrees With Max Distance Between Cities
Hard

There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

 

Example 1:



Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.
Example 2:

Input: n = 2, edges = [[1,2]]
Output: [1]
Example 3:

Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]
 

Constraints:

2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
"""
from typing import List
from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        edges2 = defaultdict(list) #direct access node edges in O(1) instead of traversing all edges
        for a,b in edges:
            edges2[a].append(b)
            edges2[b].append(a)

        def bfs(root,nodes): #bfs returning max depth and first node on last layer
            level = [root] #bfs-queue
            seen = {root} #dont use again flags
            d = 0 #depth
            while True: #do while
                nextLevel = []
                for node in level: #bfs
                    for other in edges2[node]: #children
                        if nodes[other-1]==True and other not in seen: #children not deleted or used already
                            seen.add(other) #mark as used
                            nextLevel.append(other) #add to next bfs queue
                if nextLevel: #continue
                    d += 1 #next depth reached
                    level = nextLevel #take over children as bfs queue/layer
                else: break #done with bfs
            return level[0],d #first node + depth from root

        seen = set() #dont reuse same combinations
        def rec(nodes=[True for _ in range(n)]): #what dist is left with given connected nodes
            seen.add(str(nodes)) #never eval this combination again
            if sum(nodes)==1: return #deleted to much
            for i,b in enumerate(nodes):
                if b==True: #pick first node left as root
                    root = i+1
                    break
            #double bfs=>max-depth-node yiels max dist
            #also we have both reached nodes and the path between has the distance!
            other,_ = bfs(root,nodes) #first bfs
            _,dist = bfs(other,nodes) #second bfs
            res[dist-1] += 1 #save another subtree got this dist

            for i,b in enumerate(nodes): #try to delete nodes
                if b==True: #this one is left
                    node = i+1 #the node value 1-indexed
                    reaches = 0 #counter
                    for other in edges2[node]: #connected nodes
                        if nodes[other-1]==True: #is not yet deleted
                            reaches += 1 #add as connected node
                    #leafs can get deleted!
                    if reaches==1: #leafs have exactly 1 connection
                        new = list(nodes) #unlinked copy for more readable recursion
                        new[node-1] = False #flip deletable => smaller nodes combination
                        if str(new) not in seen: #this combination is new!
                            rec(new) #get max dist for subset also


        res = [0 for _ in range(1,n)] #counts of max dists from 1 to n-1
        rec() #recursivley use all subtrees
        return res #return counts