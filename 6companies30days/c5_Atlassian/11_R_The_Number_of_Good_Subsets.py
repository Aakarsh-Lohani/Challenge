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
from itertools import combinations
from collections import Counter, defaultdict
import math
from typing import List

def dfs(frequencies, number, good_numbers, result):
    if number > 30:
        return
    frequency = frequencies[number]
    if frequency:
        for other_number in list(result.keys()):
            product = number * other_number
            if product in good_numbers:
                result[product] += result[other_number] * frequency
    dfs(frequencies, number + 1, good_numbers, result)

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) # 10
        good_numbers = set() # 1024
        for i in range(1, len(primes) + 1):
            for combo in combinations(primes, i):
                good_numbers.add(math.prod(combo))
        frequencies = Counter(nums)
        good_subsets = Counter({1 : 1})
        dfs(frequencies, 2, good_numbers, good_subsets)
        special_case = 2 ** frequencies[1] # number of 1s if a special case
        del good_subsets[1]
        return sum(value * special_case for value in good_subsets.values()) % (10 ** 9 + 7) 