#https://leetcode.com/problems/erect-the-fence/description/
"""
587. Erect the Fence
Hard

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

Fence the entire garden using the minimum length of rope, as it is expensive. The garden is well-fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter. You may return the answer in any order.

 

Example 1:


Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation: All the trees will be on the perimeter of the fence except the tree at [2, 2], which will be inside the fence.
Example 2:


Input: trees = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
Explanation: The fence forms a line that passes through all the trees.
 

Constraints:

1 <= trees.length <= 3000
trees[i].length == 2
0 <= xi, yi <= 100
All the given positions are unique.
"""
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Sort the trees by x-coordinate (and by y-coordinate if x-coordinates are the same)
        trees.sort(key=lambda p: (p[0], p[1]))

        # Initialize the upper and lower hulls
        upper = []
        lower = []

        # Compute the upper hull
        for tree in trees:
            while len(upper) >= 2 and self.cross_product(upper[-2], upper[-1], tree) < 0:
                upper.pop()
            upper.append(tree)

        # Compute the lower hull
        for tree in reversed(trees):
            while len(lower) >= 2 and self.cross_product(lower[-2], lower[-1], tree) < 0:
                lower.pop()
            lower.append(tree)

        # Combine the upper and lower hulls
        return list(set(map(tuple, upper + lower)))

    def cross_product(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])