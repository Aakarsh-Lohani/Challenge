#https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/
"""
497. Random Point in Non-overlapping Rectangles
Medium

You are given an array of non-overlapping axis-aligned rectangles rects where rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner point of the ith rectangle and (xi, yi) is the top-right corner point of the ith rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.

Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.

Note that an integer point is a point that has integer coordinates.

Implement the Solution class:

Solution(int[][] rects) Initializes the object with the given rectangles rects.
int[] pick() Returns a random integer point [u, v] inside the space covered by one of the given rectangles.
 

Example 1:


Input
["Solution", "pick", "pick", "pick", "pick", "pick"]
[[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
Output
[null, [1, -2], [1, -1], [-1, -2], [-2, -2], [0, 0]]

Explanation
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // return [1, -2]
solution.pick(); // return [1, -1]
solution.pick(); // return [-1, -2]
solution.pick(); // return [-2, -2]
solution.pick(); // return [0, 0]
 

Constraints:

1 <= rects.length <= 100
rects[i].length == 4
-10^9 <= ai < xi <= 10^9
-10^9 <= bi < yi <= 10^9
xi - ai <= 2000
yi - bi <= 2000
All the rectangles do not overlap.
At most 10^4 calls will be made to pick.
"""
import random
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = []
        total_points = 0
        for x1, y1, x2, y2 in rects:
            total_points += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(total_points)

    def pick(self) -> List[int]:
        rand = random.randint(1, self.ranges[-1])
        rect_idx = self.binary_search(rand)
        x1, y1, x2, y2 = self.rects[rect_idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]

    def binary_search(self, rand):
        left, right = 0, len(self.ranges) - 1
        while left < right:
            mid = (left + right) // 2
            if rand <= self.ranges[mid]:
                right = mid
            else:
                left = mid + 1
        return left