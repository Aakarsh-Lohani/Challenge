#https://leetcode.com/problems/constrained-subsequence-sum/description/
"""
1425. Constrained Subsequence Sum
Hard

Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].
Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.
Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].
 

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        dq = deque([0])

        for i in range(1, len(nums)):
            # pop elements from the deque that are out of the current window
            while dq and dq[0] < i - k:
                dq.popleft()

            # dp[i] is either the current number nums[i] itself
            # or nums[i] + maximum sum of the subsequence within the window
            dp[i] = nums[i] + max(dp[dq[0]], 0) if dq else nums[i]

            # pop elements from the deque that are less than the current dp[i]
            while dq and dp[i] > dp[dq[-1]]:
                dq.pop()

            dq.append(i)
            max_sum = max(max_sum, dp[i])

        return max_sum
    