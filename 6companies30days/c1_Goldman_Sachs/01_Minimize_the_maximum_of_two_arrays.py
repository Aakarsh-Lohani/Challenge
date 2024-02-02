# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description/
"""
2513. Minimize the Maximum of Two Arrays
Solved
Medium

We have two arrays arr1 and arr2 which are initially empty. You need to add positive integers to them such that they satisfy all the following conditions:

arr1 contains uniqueCnt1 distinct positive integers, each of which is not divisible by divisor1.
arr2 contains uniqueCnt2 distinct positive integers, each of which is not divisible by divisor2.
No integer is present in both arr1 and arr2.
Given divisor1, divisor2, uniqueCnt1, and uniqueCnt2, return the minimum possible maximum integer that can be present in either array.

 

Example 1:

Input: divisor1 = 2, divisor2 = 7, uniqueCnt1 = 1, uniqueCnt2 = 3
Output: 4
Explanation: 
We can distribute the first 4 natural numbers into arr1 and arr2.
arr1 = [1] and arr2 = [2,3,4].
We can see that both arrays satisfy all the conditions.
Since the maximum value is 4, we return it.
Example 2:

Input: divisor1 = 3, divisor2 = 5, uniqueCnt1 = 2, uniqueCnt2 = 1
Output: 3
Explanation: 
Here arr1 = [1,2], and arr2 = [3] satisfy all conditions.
Since the maximum value is 3, we return it.
Example 3:

Input: divisor1 = 2, divisor2 = 4, uniqueCnt1 = 8, uniqueCnt2 = 2
Output: 15
Explanation: 
Here, the final possible arrays can be arr1 = [1,3,5,7,9,11,13,15], and arr2 = [2,6].
It can be shown that it is not possible to obtain a lower maximum satisfying all conditions. 
 

Constraints:

2 <= divisor1, divisor2 <= 10^5
1 <= uniqueCnt1, uniqueCnt2 < 10^9
2 <= uniqueCnt1 + uniqueCnt2 <= 10^9
"""
import math
class Solution:

    def calculateLCM(self, a, b):
        return (a * b) // math.gcd(a, b)

    def calculateMax(self, count, divisor1, divisor2=1):
        lcm_result = self.calculateLCM(divisor1, divisor2)
        return count + count // (lcm_result - 1) - (0 if count % (lcm_result - 1) else 1)

    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        return max(
            self.calculateMax(uniqueCnt1, divisor1),
            self.calculateMax(uniqueCnt2, divisor2),
            self.calculateMax(uniqueCnt1 + uniqueCnt2, divisor1, divisor2)
        )

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimizeSet(2, 4, 8, 2))
    
# The provided Python code is part of a class Solution that contains three methods: calculateLCM, calculateMax, and minimizeSet.

# The calculateLCM method calculates the least common multiple (LCM) of two numbers a and b. The LCM is the smallest number that is a multiple of both a and b. This method uses the formula lcm(a, b) = a * b / gcd(a, b), where gcd(a, b) is the greatest common divisor of a and b. The GCD is calculated by a function not shown in the provided code.

# The calculateMax method calculates a value based on the parameters count, divisor1, and divisor2 (which defaults to 1 if not provided). First, it calculates the LCM of divisor1 and divisor2 using the calculateLCM method. Then, it calculates and returns the expression count + count // (lcm_result - 1) - (0 if count % (lcm_result - 1) else 1). This expression adds count to the integer division of count by lcm_result - 1, and subtracts 1 if count is divisible by lcm_result - 1, or 0 otherwise.

# The minimizeSet method takes four parameters: divisor1, divisor2, uniqueCnt1, and uniqueCnt2. It returns the maximum of three values calculated by the calculateMax method: the first with parameters uniqueCnt1 and divisor1, the second with parameters uniqueCnt2 and divisor2, and the third with parameters uniqueCnt1 + uniqueCnt2, divisor1, and divisor2. This method is likely used to find the maximum value that can be obtained by applying the calculateMax method to the unique elements in two sets with given divisors.