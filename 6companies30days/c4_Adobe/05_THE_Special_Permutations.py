#https://leetcode.com/problems/special-permutations/description/
""" #special case
2741. Special Permutations
Medium

You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
Return the total number of special permutations. As the answer could be large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.
 

Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 10^9
"""

#1 memory best but very high time
import math
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        mask = 1 << n

        dp = [[0] * mask for _ in range(n)]
        
        for i in range(n):
            dp[i][(1<<i)] = 1
        
        factors=[[0] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0:
                    factors[i].append(1<<j)
        
        for m in range(mask):
            for i in range(n):
                if (m >> i) & 1:
                    prevmask = m^(1<<i)
                    for factor in factors[i]:
                        if factor & prevmask:
                            for j in range(n):
                                if (factor >> j) & 1 and (prevmask >> j) & 1:
                                    dp[i][m] += dp[j][prevmask]
                                    dp[i][m] %= mod
        return sum(dp[i][mask-1] for i in range(n)) % mod

# 2 memory best time best

from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)
        mask = 1 << n

        dp = [[0] * mask for _ in range(n)]
        
        for i in range(n):
            dp[i][(1<<i)] = 1
        
        factors = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    factors[i].append(j)
        
        for m in range(mask):
            for i in range(n):
                if (m >> i) & 1:
                    prevmask = m ^ (1 << i)
                    for j in factors[i]:
                        if (prevmask >> j) & 1:
                            dp[i][m] += dp[j][prevmask]
                            dp[i][m] %= mod
        return sum(dp[i][mask-1] for i in range(n)) % mod






# 3. Memory Exceeded
from typing import List

class Solution:
    def cnt(self, last: int, mask: int) -> int:
        if mask == (1 << len(self.nums)) - 1:
            return 1
        if self.dp[last][mask] != -1:
            return self.dp[last][mask]
        res = 0
        for i in range(len(self.nums)):
            if mask & (1 << i) == 0 and (last % self.nums[i] == 0 or self.nums[i] % last == 0):
                res = (res + self.cnt(self.nums[i], mask | (1 << i))) % (10**9 + 7)
        self.dp[last][mask] = res
        return res

    def specialPerm(self, nums: List[int]) -> int:
        self.nums, self.dp = sorted(nums), [[-1 for _ in range(1 << len(nums))] for _ in range(max(nums) + 1)]
        return sum(self.cnt(num, 1 << i) for i, num in enumerate(self.nums)) % (10**9 + 7)