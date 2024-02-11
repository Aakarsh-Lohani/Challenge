#https://leetcode.com/problems/the-number-of-good-subsets/description/
"""
1994. The Number of Good Subsets
Hard

You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.
Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 30
"""
from typing import List
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
    MOD = 10**9 + 7
    freq = [0]*31
    for num in nums:
        freq[num] += 1
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    composite = {4: [2, 2], 6: [2, 3], 8: [2, 2, 2], 9: [3, 3], 10: [2, 5], 12: [2, 2, 3], 14: [2, 7], 15: [3, 5], 18: [2, 3, 3], 20: [2, 2, 5], 21: [3, 7], 22: [2, 11], 25: [5, 5], 26: [2, 13], 27: [3, 3, 3], 28: [2, 2, 7], 30: [2, 3, 5]}
    dp = [0]*(1<<15)
    dp[0] = 1
    for mask in range(1<<15):
        for i in range(15):
            if mask & (1<<i) == 0:
                continue
            if i < 11 and dp[mask^(1<<i)]:
                dp[mask] += dp[mask^(1<<i)] * freq[prime[i]]
            if i >= 11 and all((mask & (1<<prime.index(p))) for p in composite[prime[i]]):
                dp[mask] += dp[mask^(1<<i)] * freq[prime[i]]
            dp[mask] %= MOD
    return (sum(dp) * pow(2, freq[1], MOD) - 1) % MOD