#https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/description/
"""
2400. Number of Ways to Reach a Position After Exactly k Steps
Medium

You are given two positive integers startPos and endPos. Initially, you are standing at position startPos on an infinite number line. With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k, return the number of different ways to reach the position endPos starting from startPos, such that you perform exactly k steps. Since the answer may be very large, return it modulo 10^9 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.

 

Example 1:

Input: startPos = 1, endPos = 2, k = 3
Output: 3
Explanation: We can reach position 2 from 1 in exactly 3 steps in three ways:
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
It can be proven that no other way is possible, so we return 3.
Example 2:

Input: startPos = 2, endPos = 5, k = 10
Output: 0
Explanation: It is impossible to reach position 5 from position 2 in exactly 10 steps.
 

Constraints:

1 <= startPos, endPos, k <= 1000
"""
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (2 * startPos + k + 1) for _ in range(k + 1)]
        dp[0][startPos] = 1

        for i in range(1, k + 1):
            for j in range(1, 2 * startPos + k):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) 

        return dp[k][endPos] 
    
if __name__=="__main__":
    solution=Solution()
    print(solution.numberOfWays(467,113,1000))