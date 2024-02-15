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
    def numberOfWays(self, a, b, k):
        if (a - b - k) % 2: return 0
        return comb(k, (b - a + k) // 2) % (10 ** 9 + 7)
    
if __name__=="__main__":
    solution=Solution()
    print(solution.numberOfWays(467,113,1000))

""" 
# Another approach slower than the above one
class Solution:

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        mod = 10**9+7
        def nCr(n: int, r:int) ->int:
            if(r == 0):
                return 1
            v = [0] * (n+1)
            v[0] = 1
            for i in range(1, n+1):
                for j in range(r, 0, -1):
                    v[j] = ((v[j] % mod) + (v[j-1] % mod)) % mod
            return v[r]
        diff = abs(startPos -  endPos)
        if(diff > k or diff + k & 1):
            return 0
        r = (diff + k)//2
        return(nCr(k, r))
"""