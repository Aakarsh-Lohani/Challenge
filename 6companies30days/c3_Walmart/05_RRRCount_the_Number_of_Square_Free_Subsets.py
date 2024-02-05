#https://leetcode.com/problems/count-the-number-of-square-free-subsets/description/
"""
2572. Count the Number of Square-Free Subsets
Medium

You are given a positive integer 0-indexed array nums.

A subset of the array nums is square-free if the product of its elements is a square-free integer.

A square-free integer is an integer that is divisible by no square number other than 1.

Return the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 10^9 + 7.

A non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [3,4,4,5]
Output: 3
Explanation: There are 3 square-free subsets in this example:
- The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.
Example 2:

Input: nums = [1]
Output: 1
Explanation: There is 1 square-free subset in this example:
- The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 30
"""
from typing import List

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX = 61
        N = len(nums)

        # Precalculate factorization information.
        factorization = [[0]*MAX for _ in range(MAX)]
        for x in range(2, MAX):
            if factorization[x][x]: continue
            for y in range(x, MAX, x):
                factorization[y][x] += 1
                
        # Precalculate powers of 2 (mod MOD).
        power = [1]
        for _ in range(N):
            power.append(power[-1] * 2 % MOD)

        # Count number of occurrences of each number.
        count = [0]*MAX
        for x in nums:
            count[x] += 1

        # dp[i] will be the number of subsets with product i.
        dp = [0]*MAX
        dp[1] = 1

        for x in range(2, MAX):
            if not count[x]: continue
            
            # Calculate number of subsets with and without number x.
            with_x = without_x = 0
            for v in range(MAX-1, -1, -1):
                tmp = dp[v] * power[count[x]-1] % MOD
                if factorization[v][x] <= 1:
                    with_x += dp[v] * power[count[x]-1] % MOD
                    with_x %= MOD
                without_x += tmp
                without_x %= MOD
                
                if factorization[v][x] and v * x < MAX:    # Adding check to prevent out of bound error
                    dp[v*x] += tmp
                    dp[v*x] %= MOD
            
            dp[x] += with_x
            dp[x] %= MOD

            # Subtract number of subsets without current number from all subsets.
            for v in range(MAX):
                dp[v] += MOD - without_x
                dp[v] %= MOD

        return sum(dp) % MOD
nums = [3,4,4,5]
solution = Solution()
result = solution.squareFreeSubsets(nums)
print(result)